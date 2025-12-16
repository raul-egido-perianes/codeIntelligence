# graph/states/ask_name.py
from graph.state_machine import ChatState

def ask_name(state: ChatState) -> ChatState:
    state["response"] = "Por favor, dime tu nombre:"
    return state
