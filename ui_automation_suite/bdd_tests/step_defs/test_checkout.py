import logging

from pytest_bdd import parsers, scenarios, then, when

from ui_automation_suite.bdd_tests.page_objects.checkout_page import CheckoutPage
from ui_automation_suite.settings.constants import (
    CHECKOUT_STEP_1_PAGE,
    CHECKOUT_STEP_1_PAGE_TITLE,
    CHECKOUT_STEP_2_PAGE,
    CHECKOUT_STEP_2_PAGE_TITLE,
)

# Link to the feature file
scenarios("../features/checkout.feature")


@when(parsers.cfparse("user fills in {form_field}"))
def fill_form_fields(form_field, checkout_page: CheckoutPage):
    form_field = form_field.lower()
    assert form_field.lower() in [
        "first name",
        "last name",
        "postal code",
    ], f"Invalid form field: {form_field}"
    assert checkout_page.mandatory_field_is_displayed(
        form_field.lower()
    ), f"Form field {form_field} is not displayed"
    checkout_page.fill_form_field(form_field)
    logging.info(f"user fills in {form_field}")


@when("user clicks on Continue")
def click_continue(checkout_page: CheckoutPage):
    checkout_page.click_continue()
    logging.info("User clicked on Continue button")


@when("user clicks on Cancel")
def click_cancel(checkout_page: CheckoutPage):
    checkout_page.click_cancel()
    logging.info("User clicked on Cancel button")


@when("user clicks on shopping cart icon")
def click_shopping_cart_icon(checkout_page: CheckoutPage):
    checkout_page.click_cart_icon()
    logging.info("User clicked on Shopping cart icon")


@then(parsers.cfparse("error message '{mandatory_field} is required' is displayed"))
def add_product_to_cart(mandatory_field, checkout_page: CheckoutPage):
    assert checkout_page.error_displayed(), "Error message is not displayed"
    displayed_error_message = checkout_page.get_displayed_error_message()
    logging.info(f"Displayed error message: {displayed_error_message}")

    error_messages = {
        "First Name": "Error: First Name is required",
        "Last Name": "Error: Last Name is required",
        "Postal Code": "Error: Postal Code is required",
    }
    expected_error_message = error_messages[mandatory_field]

    assert (
        expected_error_message == displayed_error_message
    ), f"Expected: '{expected_error_message}' | Displayed: '{displayed_error_message}'"


@then(parsers.cfparse("user lands on checkout {checkout_name}"))
def checkout_step_one(checkout_name, checkout_page: CheckoutPage):
    assert checkout_name in [
        "Information",
        "Overview",
    ], f"Invalid checkout step: {checkout_name}"
    if checkout_name == "Information":
        page_url = CHECKOUT_STEP_1_PAGE
        page_title = CHECKOUT_STEP_1_PAGE_TITLE
    else:
        page_url = CHECKOUT_STEP_2_PAGE
        page_title = CHECKOUT_STEP_2_PAGE_TITLE

    assert (
        page_url in checkout_page.get_current_url()
    ), f"User did not land on 'Checkout: {checkout_name}' page"
    logging.info(f"User landed on 'Checkout: {checkout_name}' page")

    displayed_page_title = checkout_page.get_displayed_page_title()
    assert (
        displayed_page_title == page_title
    ), f"Expected header: {page_title}, but got: {page_title}"
