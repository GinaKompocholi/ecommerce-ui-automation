from ui_automation_suite.bdd_tests.page_objects.base_page import BasePage
from ui_automation_suite.bdd_tests.page_objects.cart_list import CartList


class ShoppingCartPage(BasePage):
    # LOCATORS
    SHOPPING_CART_BUTTON = "[data-test='shopping-cart-link']"
    CART_CONTENTS = "[data-test='cart-contents-container']"
    CART_CONTINUE_SHOPPING_BUTTON = "[data-test='continue-shopping']"
    CART_CHECKOUT_BUTTON = "[data-test='checkout']"

    def __init__(self, page):
        super().__init__(page)  # Call BasePage's initializer
        # CartList class is a component of the shopping cart class
        self.cart_list = CartList(page)  # Composition design principle

    def click_on_shopping_cart(self):
        self.page.click(self.SHOPPING_CART_BUTTON)

    def shopping_cart_is_displayed(self):
        return self.page.is_visible(self.CART_CONTENTS)

    def cart_checkout_is_displayed(self):
        return self.page.is_visible(self.CART_CHECKOUT_BUTTON)

    def continue_shopping_is_displayed(self):
        return self.page.is_visible(self.CART_CONTINUE_SHOPPING_BUTTON)

    def continue_shopping(self):
        self.page.click(self.CART_CONTINUE_SHOPPING_BUTTON)

    def click_checkout(self):
        self.page.click(self.CART_CHECKOUT_BUTTON)
