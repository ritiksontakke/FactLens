from dotenv import load_dotenv
from langchain.agents import create_agent

from src.tools.tavilyTool import tavily_search_tool

load_dotenv()

research_agent = create_agent(
    model="openai:gpt-5-nano",
    tools=[tavily_search_tool],
    system_prompt=(
        "You are a web research assistant. "
        "Search the web, prioritize official and reliable sources, "
        "verify facts, and include source URLs in your answers. "
        "Clearly state when information cannot be verified."
    ),
)


def research_query(user_input: str) -> str:
    result = research_agent.invoke(
        {
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }
    )

    return result["messages"][-1].content
