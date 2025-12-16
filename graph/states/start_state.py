from graph.types import ChatState

def start_state(state: ChatState) -> ChatState:
    state["response"] = "Bienvenido a la tienda. ¿Qué deseas hacer?"
    return state
