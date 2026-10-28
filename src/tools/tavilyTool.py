from langchain_tavily import TavilySearch
from langchain.tools import tool



@tool("tavily_search_tool")
def tavily_search_tool():
    """User this tool to do search the web"""
    return TavilySearch(
        max_results=5,
        topic="general",
    )