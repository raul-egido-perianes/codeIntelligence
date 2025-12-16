from graph.types import ChatState

def router(state: ChatState) -> ChatState:
    text = state["user_input"].lower()

    if "ver productos" in text:
        state["intent"] = "SHOW_CATALOG"
    elif "añadir" in text or "agrega" in text:
        state["intent"] = "ADD_TO_CART"
    elif "eliminar" in text or "agrega" in text:
        state["intent"] = "REMOVE_FROM_CART"
    elif "modificar" in text or "agrega" in text:
        state["intent"] = "EDIT_CART"
    elif "ver carrito" in text:
        state["intent"] = "SHOW_CART"
    elif "finalizar" in text:
        state["intent"] = "CHECKOUT"
    elif "salir" in text:
        state["intent"] = "EXIT"
    elif "help" in text:
        state["intent"] = "HELP"
    else:
        state["intent"] = "FALLBACK"

    return state

