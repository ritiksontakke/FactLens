from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import after_agent
from dotenv import load_dotenv
import os
load_dotenv()

class State(AgentState):
    agent_one_output: str

@after_agent
def update_agent_one_state(state : State, runtime):
    print("Runtime : ", runtime)
    return {
        "agent_one_output" : "Testing for agent one"
    }


research_agent = create_agent(
    model="gpt-5.4-nano",

    middleware=[update_agent_one_state],

    state_schema=State,

    system_prompt="""
    You are FactLens Research Agent.

    Your responsibility is to research the user's query
    using web search.

    Instructions:

    1. Search for relevant information.
    2. Prefer official documentation, government websites,
       research papers and trusted primary sources.
    3. Collect the latest available information.
    4. Preserve source URLs.
    5. Include publication dates when available.
    6. Avoid unsupported claims.
    7. Do not invent facts or sources.
    8. If information cannot be verified, clearly mention it.

    Return your research findings in a structured format.

    Include:
    - Information
    - Source title
    - Source URL
    - Publication date if available
    """
)

result = research_agent.invoke(
    {"messages": [{"role": "user", "content": "What about tomorrow?"}]}
)

print("result :", result["messages"][-1].content)
