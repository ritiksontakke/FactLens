from langchain.agents import create_agent

from src.tools.tavilyTool import tavily_search_tool
from src.state.agent_state import MyState
from src.middleware.agent_hooks import filter_after_agent
from src.utils.models import get_model


def filter_agent():

    print("\n[FILTER AGENT] Creating agent...")

    agent = create_agent(
        model=get_model(),
        tools=[tavily_search_tool],
        state_schema=MyState,
        middleware=[filter_after_agent],

        system_prompt="""
        You are FactLens Filter Agent.

        Remove duplicate and irrelevant information.
        Check important claims against reliable sources.
        Prefer official and latest sources.
        Remove clearly false or unsupported information.
        Preserve useful facts and source URLs.

        Return a normal, clean conversational answer.
        Do not create a verification report.
        Do not use unnecessary headings.
        """
    )

    print("[FILTER AGENT] Agent created successfully")
    print("[FILTER AGENT] Tools:", [t.name for t in [tavily_search_tool]])

    return agent


def filter_Agent(user_input: str):

    print("\n" + "#" * 60)
    print("[FILTER AGENT] STARTED")

    print("[FILTER AGENT] Received Research Information:")
    print(user_input)

    try:

        agent = filter_agent()

        result = agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        })

        print("\n[FILTER AGENT] COMPLETED")

        print("[FILTER AGENT] Final Filtered Output:")
        print(result["messages"][-1].content)

        print("[FILTER AGENT] State:")
        print("Filtered Results:", result.get("filtered_results"))

        return result

    except Exception as e:

        print("[FILTER AGENT ERROR]", str(e))
        raise

    finally:
        print("[FILTER AGENT] FINISHED")
        print("#" * 60)