from ui_automation_suite.bdd_tests.page_objects.base_page import BasePage
from ui_automation_suite.bdd_tests.page_objects.cart_list import CartList


class CheckoutPage(BasePage):
    # COMMON LOCATORS
    PAGE_TITLE = "[data-test='title']"
    CONTINUE_BUTTON = "[data-test='continue']"
    CANCEL_BUTTON = "[data-test='cancel']"
    SHOPPING_CART_ICON = "[data-test='shopping-cart-link']"

    # CHECKOUT-STEP-ONE: YOUR INFORMATION
    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-test='lastName']"
    POSTAL_CODE = "[data-test='postalCode']"
    ERROR_BUTTON = "[data-test='error-button']"

    MANDATORY_FIELDS = {
        "first name": FIRST_NAME,
        "last name": LAST_NAME,
        "postal code": POSTAL_CODE,
    }

    MANDATORY_VALUES = {
        "first name": "Ryan",
        "last name": "Rookie",
        "postal code": "12345",
    }

    # CHECKOUT-STEP-TWO: OVERVIEW

    # Payment Information:
    PAYMENT_INFO_LABEL = "[data-test='payment-info-label']"
    # SauceCard #31337
    PAYMENT_INFO_VALUE = "[data-test='payment-info-value']"

    # Shipping Information:
    SHIPPING_INFO_LABEL = "[data-test='shipping-info-label']"
    # Free Pony Express Delivery!
    SHIPPING_INFO_VALUE = "[data-test='shipping-info-value']"

    # Price Total
    TOTAL_INFO_LABEL = "[data-test='total-info-label']"
    # Item total: $29.99
    SUBTOTAL_LABEL = "[data-test='subtotal-label']"
    # Tax: $2.40
    TAX_LABEL = "[data-test='tax-label']"
    # Total: $32.39
    TOTAL_LABEL = "[data-test='total-label']"

    FINISH_BUTTON = "[data-test='finish']"

    def __init__(self, page):
        super().__init__(page)  # Call BasePage's initializer
        self.cart_list = CartList(page)  # Composition design principle

    def fill_form_field(self, form_field):
        field = self.MANDATORY_FIELDS[form_field]
        value = self.MANDATORY_VALUES[form_field]
        self.page.fill(field, value)

    def click_continue(self):
        self.page.click(self.CONTINUE_BUTTON)

    def click_cancel(self):
        self.page.click(self.CANCEL_BUTTON)

    def click_cart_icon(self):
        self.page.click(self.SHOPPING_CART_ICON)

    def click_finish(self):
        self.page.click(self.FINISH_BUTTON)

    def error_displayed(self):
        return self.page.is_visible(self.ERROR_BUTTON)

    def get_displayed_error_message(self):
        return self.page.text_content(self.ERROR_BUTTON)

    def get_displayed_page_title(self):
        return self.page.text_content(self.PAGE_TITLE)

    def mandatory_field_is_displayed(self, field):
        return self.page.is_visible(self.MANDATORY_FIELDS[field])
