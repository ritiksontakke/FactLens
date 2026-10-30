from src.agents.researcherAgent import research_query
from langchain.agents import create_agent
from src.utils.models import get_model
from src.agents.filterAgent import filter_Agent

def orchestratorAgent():
    print("Creating orchestrator agent...")

    agent = create_agent(
        model=get_model(),
        tools=[research_query,filter_Agent]
    )

    print("Created agent type:", type(agent))

    return agent