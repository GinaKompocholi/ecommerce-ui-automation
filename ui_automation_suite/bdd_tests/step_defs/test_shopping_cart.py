import logging

from pytest_bdd import parsers, scenarios, then, when

from ui_automation_suite.bdd_tests.page_objects.shopping_cart_page import (
    ShoppingCartPage,
)

# Link to the feature file
scenarios("../features/shopping_cart.feature")


@then(parsers.cfparse("user {rule} proceed to first checkout step"))
def checkout_possibility(rule, shopping_cart_page: ShoppingCartPage):
    if rule == "can":
        assert (
            shopping_cart_page.cart_checkout_is_displayed()
        ), "Checkout button is not displayed when it should be"
    else:
        assert (
            not shopping_cart_page.cart_checkout_is_displayed()
        ), "Checkout button is displayed when it should not be"
    logging.info(f"User {rule} proceed to first checkout step")


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
