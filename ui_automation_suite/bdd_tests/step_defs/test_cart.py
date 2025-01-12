import logging

from pytest_bdd import parsers, scenarios, then, when

from ui_automation_suite.bdd_tests.page_objects.shopping_cart_page import (
    ShoppingCartPage,
)
from ui_automation_suite.settings.constants import AVAILABLE_PRODUCTS, INVALID_PRODUCT

# Link to the feature file
scenarios("../features/shopping_cart.feature")


@then(parsers.cfparse("the cart contains {cart_items_count:d} product(s)"))
def cart_contains_products(cart_items_count: int, shopping_cart_page: ShoppingCartPage):
    total_cart_items = len(shopping_cart_page.get_all_cart_products())
    assert (
        total_cart_items == cart_items_count
    ), f"Expected {cart_items_count} products, but got {total_cart_items}"
    logging.info(f"The cart contains {cart_items_count:d} product(s)")


@then(parsers.cfparse("user {rule} proceed to checkout"))
def checkout_possibility(rule, shopping_cart_page: ShoppingCartPage):
    if rule == "can":
        assert (
            shopping_cart_page.cart_checkout_is_displayed()
        ), "Checkout button is not displayed"
    else:
        assert (
            not shopping_cart_page.cart_checkout_is_displayed()
        ), "Checkout button is displayed"
    logging.info(f"User {rule} proceed to checkout")


@then(parsers.cfparse("user can continue shopping"))
def continue_shopping_possibility(shopping_cart_page: ShoppingCartPage):
    assert (
        shopping_cart_page.continue_shopping_is_displayed()
    ), "Continue shopping button is not displayed"
    logging.info("User can continue shopping")


@when(parsers.cfparse("user continues shopping"))
def continue_shopping(shopping_cart_page: ShoppingCartPage):
    shopping_cart_page.continue_shopping()
    logging.info("User continues shopping")


@then(parsers.cfparse("product {product_name} is displayed in the cart"))
def product_is_displayed_in_cart(
    product_name: str, shopping_cart_page: ShoppingCartPage
):
    assert product_name in AVAILABLE_PRODUCTS, INVALID_PRODUCT
    product = shopping_cart_page.get_specific_product(product_name)
    assert shopping_cart_page.product_name_is_visible(
        product
    ), "Product name is not displayed"
    logging.info(f"Product {product_name} is displayed in the cart")


@then(parsers.cfparse("the quantity of product {product_name} is {quantity:d}"))
def product_quantity_in_cart(
    product_name: str, quantity: int, shopping_cart_page: ShoppingCartPage
):
    assert product_name in AVAILABLE_PRODUCTS, INVALID_PRODUCT
    product = shopping_cart_page.get_specific_product(product_name)
    product_quantity_in_cart = shopping_cart_page.get_product_quantity(product)
    assert (
        product_quantity_in_cart == quantity
    ), "Unexpected quantity of product in the cart"
    logging.info(
        f"Product {product_name} quantity displayed in cart is as expected: {quantity}"
    )


@then(parsers.cfparse("the price of product {product_name} is {price}"))
def product_price_in_cart(
    product_name: str, price: str, shopping_cart_page: ShoppingCartPage
):
    assert product_name in AVAILABLE_PRODUCTS, INVALID_PRODUCT
    expected_price = float(price.replace("$", ""))
    product = shopping_cart_page.get_specific_product(product_name)
    actual_price = shopping_cart_page.get_product_price(product)
    assert actual_price == expected_price, (
        f"Expected price for product {product_name} is ${expected_price} "
        f"but the displayed price is ${actual_price}"
    )
    logging.info(
        f"Product {product_name} price displayed in cart is as expected: {actual_price}"
    )


@then(
    parsers.cfparse(
        "the full name of product {product_name} displayed is {product_full_name}"
    )
)
def product_name_in_cart(
    product_name: str, product_full_name: str, shopping_cart_page: ShoppingCartPage
):
    assert product_name in AVAILABLE_PRODUCTS, INVALID_PRODUCT
    product = shopping_cart_page.get_specific_product(product_name)
    actual_name = shopping_cart_page.get_product_name(product)
    assert actual_name == product_full_name, (
        f"Expected name for product {product_name} is '{product_full_name}' "
        f"but the displayed name is '{actual_name}'"
    )
    logging.info(
        f"The name of product {product_name} in the cart is '{product_full_name}'"
    )


@then(parsers.cfparse("user can remove product {product_name} from the cart"))
def user_can_remove_product_from_cart(
    product_name: str, shopping_cart_page: ShoppingCartPage
):
    assert product_name in AVAILABLE_PRODUCTS, INVALID_PRODUCT
    product = shopping_cart_page.get_specific_product(product_name)
    assert shopping_cart_page.can_remove_product_from_the_cart(
        product
    ), f"Product {product_name} cannot be removed from the cart"
    logging.info(f"User can remove product {product_name} from the cart")


@when(parsers.cfparse("user removes product {product_name} from the shopping cart"))
def user_removes_product_from_cart(
    product_name: str, shopping_cart_page: ShoppingCartPage
):
    assert product_name in AVAILABLE_PRODUCTS, INVALID_PRODUCT
    product = shopping_cart_page.get_specific_product(product_name)
    shopping_cart_page.remove_product_from_the_cart(product)
    logging.info(f"User removed product {product_name} from the cart")
