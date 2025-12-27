# graph/states/fallback.py
from graph.types import ChatState


def help(state: ChatState) -> ChatState:
    state["response"] = "Estas son las acciones que puedes hacer:\n" \
    "1. 'ver productos' - Para ver el catálogo de productos. \n" \
    "2. 'añadir' - Para añadir un producto al carrito. \n" \
    "3. 'eliminar' - Para eliminar un producto del carrito. \n" \
    "4. 'modificar' - Para modificar la cantidad de un producto. \n" \
    "5. 'ver carrito' - Para ver los productos existentes en el carrito. \n" \
    "6. 'finalizar' - Para continuar con el proceso de compra. \n" \
    "7. 'salir' - Para finalizar el chat. \n" \
    "8. 'help' - Para mostrar las acciones que se pueden hacer. \n"
    return state
    