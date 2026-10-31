from typing import Any

from langchain.agents.middleware import after_agent
from langgraph.runtime import Runtime

from src.state.agent_state import MyState


@after_agent(state_schema=MyState)
def research_after_agent(
    state: MyState,
    runtime: Runtime
) -> dict[str, Any] | None:

    print("\n[MIDDLEWARE] RESEARCH AFTER_AGENT TRIGGERED")

    messages = state.get("messages", [])

    if not messages:
        print("[MIDDLEWARE] No messages found")
        return None

    last_message = messages[-1]

    print("[MIDDLEWARE] Research output captured")

    return {
        "search_results": str(last_message.content),
        "search_agent_messages": messages
    }


@after_agent(state_schema=MyState)
def filter_after_agent(
    state: MyState,
    runtime: Runtime
) -> dict[str, Any] | None:

    print("\n[MIDDLEWARE] FILTER AFTER_AGENT TRIGGERED")

    messages = state.get("messages", [])

    if not messages:
        print("[MIDDLEWARE] No messages found")
        return None

    last_message = messages[-1]

    print("[MIDDLEWARE] Filtered output captured")

    return {
        "filtered_results": str(last_message.content),
        "filter_agent_messages": messages,
        "final_answer": str(last_message.content)
    }