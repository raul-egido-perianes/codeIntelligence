# tests/test_router.py
from graph.states.router_state import router
from models.cart_model import Cart

def make_state(msg):
    return {
        "user_input": msg,
        "cart": Cart(),
        "intent": "",
        "awaiting_confirmation": False,
        "awaiting_name": False,
        "awaiting_city": False,
    }

def test_router_show_catalog():
    state = make_state("ver productos")
    result = router(state)
    assert result["intent"] == "SHOW_CATALOG"

def test_router_finalizar():
    state = make_state("finalizar")
    result = router(state)
    assert result["intent"] == "CHECKOUT"
