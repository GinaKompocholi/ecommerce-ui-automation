from ui_automation_suite.bdd_tests.page_objects.base_page import BasePage


class ShoppingCartPage(BasePage):
    # LOCATORS
    SHOPPING_CART_BUTTON = "[data-test='shopping-cart-link']"
    CART_CONTENTS = "[data-test='cart-contents-container']"
    CART_CONTINUE_SHOPPING_BUTTON = "[data-test='continue-shopping']"
    CART_CHECKOUT_BUTTON = "[data-test='checkout']"
    # ITEM SPECIFIC LOCATORS
    CART_ITEM = "[data-test='inventory-item']"
    CART_ITEM_NAME = "[data-test='inventory-item-name']"
    CART_ITEM_DESCRIPTION = "[data-test='inventory-item-desc']"
    CART_ITEM_PRICE = "[data-test='inventory-item-price']"
    CART_ITEM_QUANTITY = "[data-test='item-quantity']"
    CART_ITEM_REMOVE_BUTTON = "[data-test*='remove']"

    def click_on_shopping_cart(self):
        self.page.click(self.SHOPPING_CART_BUTTON)

    def shopping_cart_is_displayed(self):
        return self.page.is_visible(self.CART_CONTENTS)

    def get_all_cart_products(self):
        return self.page.query_selector_all(self.CART_ITEM)

    def cart_checkout_is_displayed(self):
        return self.page.is_visible(self.CART_CHECKOUT_BUTTON)

    def continue_shopping_is_displayed(self):
        return self.page.is_visible(self.CART_CONTINUE_SHOPPING_BUTTON)

    def continue_shopping(self):
        self.page.click(self.CART_CONTINUE_SHOPPING_BUTTON)

    def checkout(self):
        self.page.click(self.CART_CHECKOUT_BUTTON)

    def get_specific_product(self, wanted_product):
        products = self.get_all_cart_products()
        for product in products:
            product_name = (
                product.query_selector(self.CART_ITEM_NAME).text_content().strip()
            )
            if wanted_product in product_name:
                return product

    def product_name_is_visible(self, product):
        """Checks if the product name is visible within the product element."""
        name = product.query_selector(self.CART_ITEM_NAME)
        return name is not None and name.is_visible()

    def get_product_quantity(self, product) -> int:
        """Get the quantity of a specific product in the cart."""
        quantity = product.query_selector(self.CART_ITEM_QUANTITY)
        return int(quantity.text_content())

    def get_product_price(self, product) -> float:
        """Get the price of a specific product in the cart."""
        price = product.query_selector(self.CART_ITEM_PRICE)
        return float(price.text_content().replace("$", ""))

    def get_product_name(self, product) -> str:
        """Get the full name of a specific product in the cart."""
        name = product.query_selector(self.CART_ITEM_NAME)
        return name.text_content()

    def can_remove_product_from_the_cart(self, product):
        """Check if the remove button is visible for a specific product in the cart."""
        remove_product_btn = product.query_selector(self.CART_ITEM_REMOVE_BUTTON)
        return remove_product_btn is not None and remove_product_btn.is_visible()

    def remove_product_from_the_cart(self, product):
        product.query_selector(self.CART_ITEM_REMOVE_BUTTON).click()
