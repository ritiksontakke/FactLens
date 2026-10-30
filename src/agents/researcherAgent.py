from langchain.agents import create_agent

from src.tools.tavilyTool import tavily_search_tool
from src.state.agent_state import MyState
from src.utils.models import get_model
from langchain.tools import tool


@tool("research_agent")
def research_query(user_input: str):
    """
    You are a web research assistant.
    """
    research_agent = create_agent(
    model=get_model(),
    tools=[tavily_search_tool],
    state_schema=MyState,
    system_prompt=(
        "You are a web research assistant. "
        "Search the web, prioritize official and reliable sources, "
        "verify facts, and include source URLs in your answers. "
        "Clearly state when information cannot be verified."
    ),
)
    

    result = research_agent.invoke(
        {
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }
    )
    return result["messages"][-1].content
