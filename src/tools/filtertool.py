from langchain.tools import tool

@tool("filter_tool")
def search(query: str) -> str:
    """."""
    return f"Results for: {query}"