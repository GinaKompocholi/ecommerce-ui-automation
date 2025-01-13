from ui_automation_suite.bdd_tests.page_objects.base_page import BasePage


# Handles logic and validations specific to the cart list component.
class CartList(BasePage):
    # ITEM SPECIFIC LOCATORS
    CART_ITEM = "[data-test='inventory-item']"
    CART_ITEM_NAME = "[data-test='inventory-item-name']"
    CART_ITEM_DESCRIPTION = "[data-test='inventory-item-desc']"
    CART_ITEM_PRICE = "[data-test='inventory-item-price']"
    CART_ITEM_QUANTITY = "[data-test='item-quantity']"
    CART_ITEM_REMOVE_BUTTON = "[data-test*='remove']"

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

    def remove_product_button_is_visible(self, product):
        """Check if the remove button is visible for a specific product in the cart."""
        remove_product_btn = product.query_selector(self.CART_ITEM_REMOVE_BUTTON)
        return remove_product_btn is not None and remove_product_btn.is_visible()

    def get_all_cart_products(self):
        return self.page.query_selector_all(self.CART_ITEM)

    def get_specific_product(self, wanted_product, all_products):
        for product in all_products:
            product_name = (
                product.query_selector(self.CART_ITEM_NAME).text_content().strip()
            )
            if wanted_product in product_name:
                return product

    def remove_product_from_the_cart(self, product):
        product.query_selector(self.CART_ITEM_REMOVE_BUTTON).click()
