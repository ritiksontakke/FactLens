import os
import json
from pathlib import Path

from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain.tools import tool


# Load .env from FactLens root
BASE_DIR = Path(__file__).resolve().parents[2]

ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH, override=True)

print("\n========== ENV DEBUG ==========")
print("ENV PATH:", ENV_PATH)
print("ENV EXISTS:", ENV_PATH.exists())
print(
    "TAVILY KEY:",
    "LOADED" if os.getenv("TAVILY_API_KEY") else "MISSING"
)
print("===============================\n")

@tool("tavily_search_tool")
def tavily_search_tool(query: str) -> str:
    """
    Search the web using Tavily and return relevant
    search results with source URLs and information.
    """

    print("\n[TOOL] TAVILY SEARCH STARTED")
    print("[TOOL] Query:", query)

    try:
        api_key = os.getenv("TAVILY_API_KEY")

        if not api_key:
            raise ValueError("TAVILY_API_KEY missing")

        tavily = TavilySearch(
            tavily_api_key=api_key,
            max_results=8,
            topic="general"
        )

        results = tavily.invoke({
            "query": query
        })

        print("[TOOL] SEARCH SUCCESSFUL")
        print("[TOOL] RESULTS:", results)

        return json.dumps(
            results,
            ensure_ascii=False,
            default=str
        )

    except Exception as e:
        print("[TOOL ERROR]", repr(e))
        raise

    finally:
        print("[TOOL] TAVILY SEARCH FINISHED")