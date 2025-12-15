import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from models.catalog import get_all_products, get_product_by_id, search_products_by_name

def test_get_all_products():
    products = get_all_products()
    assert len(products) == 25


def test_get_product_by_id():
    product = get_product_by_id("P001")
    assert product is not None
    assert product["name"] == "Camiseta básica"

def test_serch_products_by_name():
    product = search_products_by_name("Camiseta básica")
    assert product is not None
