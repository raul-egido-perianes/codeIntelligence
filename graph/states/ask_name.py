# graph/states/ask_name.py
from graph.types import ChatState


def ask_name(state: ChatState) -> ChatState:
    state["response"] = "Por favor, dime tu nombre:"
    state["awaiting_name"] = True
    return state
