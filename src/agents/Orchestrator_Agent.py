from src.agents.researcherAgent import research_query
from src.agents.filterAgent import filter_Agent


def orchestratorAgent(user_query: str):

    print("\n")
    print("*" * 70)
    print("FACTLENS ORCHESTRATOR STARTED")
    print("*" * 70)

    state = {
        "user_query": user_query,
        "search_results": "",
        "search_agent_messages": [],
        "filtered_results": "",
        "filter_agent_messages": [],
        "final_answer": ""
    }

    try:

        # STEP 1: RESEARCH AGENT

        print("\n[ORCHESTRATOR] STEP 1: RESEARCH AGENT")

        research_result = research_query(user_query)

        state["search_results"] = research_result.get(
            "search_results",
            str(research_result["messages"][-1].content)
        )

        state["search_agent_messages"] = research_result["messages"]

        print("[ORCHESTRATOR] Research data saved in state")

        # STEP 2: FILTER AGENT

        print("\n[ORCHESTRATOR] STEP 2: FILTER AGENT")

        filter_result = filter_Agent(
            state["search_results"]
        )

        state["filtered_results"] = filter_result.get(
            "filtered_results",
            str(filter_result["messages"][-1].content)
        )

        state["filter_agent_messages"] = filter_result["messages"]

        print("[ORCHESTRATOR] Filtered data saved in state")

        # STEP 3: FINAL ANSWER

        state["final_answer"] = state["filtered_results"]

        print("\n[ORCHESTRATOR] FINAL ANSWER:")
        print(state["final_answer"])

        print("\n[ORCHESTRATOR] ALL AGENTS COMPLETED SUCCESSFULLY")

        return state

    except Exception as e:

        print("\n[ORCHESTRATOR ERROR]", str(e))
        raise

    finally:

        print("\n")
        print("*" * 70)
        print("FACTLENS ORCHESTRATOR FINISHED")
        print("*" * 70)