import pytest
from models.cart_model import Cart
from models.catalog import get_product_by_id


@pytest.fixture
def cart():
    return Cart()

@pytest.fixture
def product():
    return get_product_by_id("P004") # Zapatillas deportivas

def test_add_product(cart, product):
    cart.add_product(product["id"], 2)
    items = cart.list_items()
    assert len(items) == 1
    assert items[0]["quantity"] == 2
    assert items[0]["id"] == "P004"

def test_remove_product(cart, product):
    cart.add_product(product["id"], 1)
    cart.remove_product("P004")
    assert cart.get_item("P004") is None
    assert len(cart.list_items()) == 0

def test_update_quantity(cart, product):
    cart.add_product(product["id"], 1)
    cart.update_quantity("P004", 5)
    assert cart.get_item("P004").quantity == 5

def test_update_quantity_to_zero(cart, product):
    cart.add_product(product["id"], 1)
    cart.update_quantity("P004", 0)
    assert cart.get_item("P004") is None

def test_get_total(cart, product):
    cart.add_product(product["id"], 3)
    total = cart.get_total()
    assert total == product["price"] * 3