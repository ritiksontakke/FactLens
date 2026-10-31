from typing_extensions import NotRequired
from langchain.agents import AgentState
from langchain.messages import AnyMessage


class MyState(AgentState):

    user_query: NotRequired[str]

    search_results: NotRequired[str]

    search_agent_messages: NotRequired[list[AnyMessage]]

    filtered_results: NotRequired[str]

    filter_agent_messages: NotRequired[list[AnyMessage]]

    final_answer: NotRequired[str]