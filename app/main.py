import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from graph.state_machine import app
from models.cart_model import Cart

state = {
    "user_input": "",
    "response": "",
    "cart": Cart(),
    "intent": "",
    "name": None,
    "city": None,
}

while True:
    print(state["response"])  # mostramos respuesta anterior
    user_input = input("Usuario: ")
    state["user_input"] = user_input

    result = app.invoke(state)
    state.update(result)

    if result.get("intent") == "EXIT":
        break
