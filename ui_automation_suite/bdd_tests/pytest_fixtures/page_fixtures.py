import pytest

from ui_automation_suite.bdd_tests.page_objects.login_page import LoginPage
from ui_automation_suite.bdd_tests.page_objects.products_page import ProductPage
from ui_automation_suite.bdd_tests.page_objects.shopping_cart_page import (
    ShoppingCartPage,
)
from ui_automation_suite.bdd_tests.page_objects.sidebar import BurgerMenu


@pytest.fixture()
def login_page(page):
    login_page = LoginPage(page)
    return login_page


@pytest.fixture()
def product_page(page):
    product_page = ProductPage(page)
    return product_page


@pytest.fixture()
def burgermenu_page(page):
    burgermenu_page = BurgerMenu(page)
    return burgermenu_page


@pytest.fixture()
def shopping_cart_page(page):
    shopping_cart_page = ShoppingCartPage(page)
    return shopping_cart_page