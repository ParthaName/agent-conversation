from crewai import Agent
from agents.base_llm import get_llm

llm = get_llm()

evaluator = Agent(
    role="Conversation Analyst",
    goal="Detect topic drift and classify conversation type",
    backstory=(
        "You analyze conversations. "
        "You detect drift from original topic. "
        "You classify type: Debate, Agreement, Speculative, Technical."
    ),
    allow_delegation=False,
    verbose=False,
    llm=llm
)
