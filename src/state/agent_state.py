from langchain.agents import AgentState
from langchain.messages import AnyMessage

class MyState(AgentState):

    user_id: str

    search_results: str

    search_agent_messages: list[AnyMessage]

    filtered_results: str

    filter_agent_messages: list[AnyMessage]