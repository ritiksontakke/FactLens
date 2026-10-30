from langchain.agents import create_agent

from src.tools.tavilyTool import tavily_search_tool
from src.state.agent_state import MyState
from src.utils.models import get_model
from langchain.tools import tool


@tool("filterAgent")
def filter_Agent(user_input: str):
    """
    you are a filter agent
    """
    research_agent = create_agent(
    model=get_model(),
    tools=[tavily_search_tool],
    state_schema=MyState,
    system_prompt="""
    You are a Filter Agent.

    Read the WebSearch Agent messages.

    Remove:
    - Duplicate information
    - Irrelevant information
    - Unnecessary content

    Preserve useful information and source URLs.
    """
)
    

    result = research_agent.invoke(
        {
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }
    )
    return result["messages"][-1].content
