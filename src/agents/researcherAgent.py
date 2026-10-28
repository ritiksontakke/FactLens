from langchain.agents import create_agent
from langchain.tools import tool
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()


@tool("tavily_search_tool")
def tavily_search_tool():
    """User this tool to do search the web"""
    return TavilySearch(
        max_results=5,
        topic="general",
    )


agent = create_agent(model="openai:gpt-5-nano", tools=[tavily_search_tool])

# user_input = "What nation hosted the Euro 2024? Include only wikipedia sources."
user_input = "Tell me about the Nagpur MLC election in Maharashtra in 2026. Provide the latest election results as of 28 October 2026, " \
"including the names of the top three candidates, their political parties, total votes received, and their winning status." \
" Use reliable and official sources to verify the information."
result = agent.invoke(
    {"messages": [{"role": "user", "content": user_input}]},
)
print("result : ", result["messages"][-1].content)