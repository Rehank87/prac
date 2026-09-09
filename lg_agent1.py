import os
from dotenv import load_dotenv
from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END

from auth import Get_Jwt

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
GPT_5_5 = os.getenv("GPT_5_5")
GPT_LUNA = os.getenv("GPT_LUNA")
GPT_TERRA = os.getenv("GPT_TERRA")
GPT_SOL = os.getenv("GPT_SOL")
TOKEN = os.getenv("TOKEN")
# TOKEN = Get_Jwt()

class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]

llm = ChatOpenAI(
    model="GPT_LUNA",
    base_url=GPT_LUNA,
    api_key=TOKEN,
    timeout=30,
)

def process(state: AgentState) -> AgentState:
    """This model will solve the request you input"""
    response = llm.invoke(state["messages"])

    state["messages"].append(AIMessage(content=response.content))
    print(f"\nAI: {response.content}")

    return state


graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

conversation_history = []

user_input = input("Enter: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages": conversation_history})
    conversation_history = result["messages"]
    user_input = input("Enter: ")