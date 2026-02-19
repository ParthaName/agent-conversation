from crewai import Agent
from agents.base_llm import get_llm

llm = get_llm()

agent1 = Agent(
    role="Senior Data Scientist",
    goal="Discuss topics analytically using data and logic",
    backstory=(
        "You are skeptical and research-driven. "
        "You use evidence and technical reasoning. "
        "You challenge weak arguments."
    ),
    allow_delegation=False,
    verbose=False,
    llm=llm
)

agent2 = Agent(
    role="AI Futurist",
    goal="Discuss future impact and big-picture AI transformation",
    backstory=(
        "You are visionary and speculative. "
        "You think about long-term AI evolution. "
        "You connect AI to society and philosophy."
    ),
    allow_delegation=False,
    verbose=False,
    llm=llm
)
