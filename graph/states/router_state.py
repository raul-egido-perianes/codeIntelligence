from graph.types import ChatState

def router(state: ChatState) -> ChatState:
    text = state["user_input"].lower()

    if state.get("intent") == "IDLE":
        return state

    if state.get("awaiting_confirmation"):
        if text in ("sí", "si"):
            state["awaiting_confirmation"] = False
            state["intent"] = "CONFIRM_YES"
        elif text in ("no", "cancelar"):
            state["awaiting_confirmation"] = False
            state["intent"] = "CONFIRM_NO"
        else:
            state["intent"] = "CONFIRM_REPEAT"
        return state

    if state.get("awaiting_name"):
        state["name"] = state["user_input"]
        state["awaiting_name"] = False
        state["intent"] = "ASK_CITY"
        return state
    
    if state.get("awaiting_city"):
        state["city"] = state["user_input"]
        state["awaiting_city"] = False
        state["intent"] = "FINAL_SUMMARY"
        return state

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

