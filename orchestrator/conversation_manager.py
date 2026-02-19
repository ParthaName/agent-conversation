from agents.discussion_agents import agent1, agent2
from agents.evaluator_agent import evaluator
from config.settings import MAX_TURNS
import time
from litellm.exceptions import RateLimitError
import re


def safe_llm_call(llm, messages, max_retries=5):
    for attempt in range(max_retries):
        try:
            return llm.call(messages)

        except RateLimitError as e:
            error_msg = str(e)
            match = re.search(r"try again in ([\d\.]+)s", error_msg)

            if match:
                wait_time = float(match.group(1)) + 0.5
            else:
                wait_time = 58

            print(f"Rate limit hit. Waiting {wait_time} seconds...")
            time.sleep(wait_time)

    raise Exception("Max retries exceeded due to rate limits.")


def generate_reply(agent, topic, history):
    messages = [
        {
            "role": "system",
            "content": f"""
You are {agent.role}.
{agent.backstory}

Rules:
- Stay aligned with the original topic: {topic}
- Do NOT repeat previous arguments.
- Add new insight.
- Keep response under 200 words.
"""
        },
        {
            "role": "user",
            "content": f"Conversation so far:\n{history}\n\nRespond now."
        }
    ]

    response = safe_llm_call(agent.llm, messages)
    return response.strip()


def evaluate(topic, history):
    messages = [
        {
            "role": "system",
            "content": """
You are a conversation evaluator.

Respond STRICTLY in this exact format:

ON_TOPIC: Yes or No
DRIFT_STARTED: Yes or No
TYPE: Debate / Agreement / Speculative / Technical / Philosophical / Repetitive
"""
        },
        {
            "role": "user",
            "content": f"""
Original Topic:
{topic}

Conversation:
{history}
"""
        }
    ]
    response = safe_llm_call(evaluator.llm, messages)
    #response = evaluator.llm.call(messages)
    return response.strip()


def run_conversation_stream(topic):
    history = f"Topic: {topic}\n\n"

    for turn in range(MAX_TURNS):

        if turn % 2 == 0:
            response = generate_reply(agent1, topic, history)
            speaker = "Agent 1 (Data Scientist)"
        else:
            response = generate_reply(agent2, topic, history)
            speaker = "Agent 2 (Futurist)"

        history += f"{speaker}:\n{response}\n\n"

        yield history, "Running..."

        # Evaluate every 2 turns
        if turn >= 2 and turn % 2 == 1:
            analysis = evaluate(topic, history)

            # SAFE drift detection
            on_topic = "ON_TOPIC: Yes" in analysis
            drift_started = "DRIFT_STARTED: Yes" in analysis

            if not on_topic or drift_started:
                yield history, f"Stopped due to drift.\n\n{analysis}"
                return

    yield history, "Max turns reached."