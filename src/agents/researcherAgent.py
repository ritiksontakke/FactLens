from langchain.agents import create_agent

from src.tools.tavilyTool import tavily_search_tool
from src.state.agent_state import MyState
from src.middleware.agent_hooks import research_after_agent
from src.utils.models import get_model


def research_agent():

    print("\n[RESEARCH AGENT] Creating agent...")

    agent = create_agent(
        model=get_model(),
        tools=[tavily_search_tool],
        state_schema=MyState,
        middleware=[research_after_agent],

        system_prompt="""
        You are FactLens Research Agent.

        Search the web.
        Prefer official and reliable sources.
        Collect latest information.
        Preserve source URLs and publication dates.
        Never invent facts.
        """
    )

    print("[RESEARCH AGENT] Agent created successfully")
    print("[RESEARCH AGENT] Tools:", [t.name for t in [tavily_search_tool]])

    return agent


def research_query(user_input: str):

    print("\n" + "#" * 60)
    print("[RESEARCH AGENT] STARTED")
    print("[RESEARCH AGENT] User Query:", user_input)

    try:

        agent = research_agent()

        result = agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            "user_query": user_input
        })

        print("\n[RESEARCH AGENT] COMPLETED")

        print("[RESEARCH AGENT] Final Output:")
        print(result["messages"][-1].content)

        print("[RESEARCH AGENT] State:")
        print("Search Results:", result.get("search_results"))

        return result

    except Exception as e:

        print("[RESEARCH AGENT ERROR]", str(e))
        raise

    finally:
        print("[RESEARCH AGENT] FINISHED")
        print("#" * 60)