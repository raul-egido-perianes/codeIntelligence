# graph/state_machine.py

from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from models.cart_model import Cart

from graph.types import ChatState
from graph.states.router_state import router
from graph.states.start_state import start_state
from graph.states.show_catalog import show_catalog
from graph.states.edit_cart import edit_cart
from graph.states.show_cart import show_cart
from graph.states.help import help
from graph.states.fallback import fallback
from graph.states.checkout_confirm import checkout_confirm
from graph.states.ask_name import ask_name
from graph.states.ask_city import ask_city
from graph.states.final_summary import final_summary

graph = StateGraph(ChatState)

graph.add_node("START", start_state)
graph.add_node("HELP", help)
graph.add_node("ROUTER", router)
graph.add_node("SHOW_CATALOG", show_catalog)
graph.add_node("EDIT_CART", edit_cart)
graph.add_node("SHOW_CART", show_cart)
graph.add_node("FALLBACK", fallback)
graph.add_node("CHECKOUT_CONFIRM", checkout_confirm)
graph.add_node("ASK_NAME", ask_name)
graph.add_node("ASK_CITY", ask_city)
graph.add_node("FINAL_SUMMARY", final_summary)

graph.set_entry_point("START")

graph.add_edge("START", "ROUTER")

graph.add_conditional_edges(
    "ROUTER",
    lambda state: state["intent"],
    {
        "SHOW_CATALOG": "SHOW_CATALOG",
        "ADD_TO_CART": "EDIT_CART",
        "EDIT_CART": "EDIT_CART",
        "REMOVE_FROM_CART": "EDIT_CART",
        "HELP": "HELP",
        "SHOW_CART": "SHOW_CART",
        "CHECKOUT": "CHECKOUT_CONFIRM",
        "FALLBACK": "FALLBACK",
        "EXIT": END,
        "ROUTER_BACK": "ROUTER",
    },
)

# graph.add_edge("SHOW_CATALOG", "ROUTER")
# graph.add_edge("EDIT_CART", "ROUTER")
# graph.add_edge("SHOW_CART", "ROUTER")
# graph.add_edge("FALLBACK", "ROUTER")
graph.add_edge("CHECKOUT_CONFIRM", "ASK_NAME")
graph.add_edge("ASK_NAME", "ASK_CITY")
graph.add_edge("ASK_CITY", "FINAL_SUMMARY")
graph.add_edge("FINAL_SUMMARY", END)

app = graph.compile()






