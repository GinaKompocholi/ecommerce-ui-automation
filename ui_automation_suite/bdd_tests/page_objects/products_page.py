from ui_automation_suite.bdd_tests.page_objects.base_page import BasePage


class ProductPage(BasePage):
    # LOCATORS
    INVENTORY_CONTAINER = "[data-test='inventory-container']"
    TOTAL_INVENTORY = "div.inventory_list .inventory_item"
    SORT_BUTTON = "[data-test='product-sort-container']"
    INVENTORY_LIST = "[data-test='inventory-list']"
    INVENTORY_ITEMS = "[data-test='inventory-item']"
    INVENTORY_ITEM_NAME = "[data-test='inventory-item-name']"
    INVENTORY_ITEM_PRICE = "[data-test='inventory-item-price']"

    INVENTORY_ITEM_DESCRIPTION = "[data-test='inventory-item-description']"
    INVENTORY_ITEM_IMAGE = "img[data-test*='mg']"
    INVENTORY_ITEM_ADD_TO_CART_BUTTON = "[data-test*='add-to-cart']"
    INVENTORY_ITEM_REMOVE_FROM_CART_BUTTON = "[data-test*='remove']"

    CART_BADGE = "[data-test='shopping-cart-badge']"

    def sort_products_by_order(self, order_type: str):
        self.page.click(self.SORT_BUTTON)
        sort_options = {
            "ascending name": "az",
            "descending name": "za",
            "ascending price": "lohi",
            "descending price": "hilo",
        }
        self.page.select_option(self.SORT_BUTTON, sort_options[order_type])

    def get_all_products(self):
        # Wait for the inventory container to appear
        self.page.wait_for_selector(self.INVENTORY_CONTAINER)
        products = self.page.query_selector_all(self.INVENTORY_ITEMS)
        return products

    def extract_product_data(self, attribute_selector, transform_fn=None):
        """
        Generic method to extract data from products.

        :param attribute_selector: Selector to extract the attribute (e.g., name or
            price).
        :param transform_fn: Function to transform the extracted data (e.g., converting
            price to float).
        :return: List of extracted and optionally transformed data.
        """
        products = self.get_all_products()
        data = []

        for product in products:
            attribute = (
                product.query_selector(attribute_selector).text_content().strip()
            )
            if transform_fn:
                attribute = transform_fn(attribute)
            data.append(attribute)

        return data

    def get_sorted_product_names(self):
        return self.extract_product_data(self.INVENTORY_ITEM_NAME)

    def get_sorted_product_prices(self):
        return self.extract_product_data(
            self.INVENTORY_ITEM_PRICE, transform_fn=lambda x: float(x.replace("$", ""))
        )

    def add_to_cart_button(self):
        return self.page.query_selector("[data-test='add-to-cart']")

    def name_is_visible(self, product):
        """Checks if the product name is visible within the product element."""
        name = product.query_selector(self.INVENTORY_ITEM_NAME)
        return name is not None and name.is_visible()

    def get_product_name(self, product):
        return product.query_selector(self.INVENTORY_ITEM_NAME).text_content().strip()

    def click_on_product_name(self, product):
        product.query_selector(self.INVENTORY_ITEM_NAME).click()

    def price_is_visible(self, product):
        """Checks if the product price is visible within the product element."""
        price = product.query_selector(self.INVENTORY_ITEM_PRICE)
        return price is not None and price.is_visible()

    def description_is_visible(self, product):
        """Checks if the product description is visible within the product element."""
        description = product.query_selector(self.INVENTORY_ITEM_DESCRIPTION)
        return description is not None and description.is_visible()

    def image_is_visible(self, product):
        """Checks if the product image is visible within the product element."""
        image = product.query_selector(self.INVENTORY_ITEM_IMAGE)
        return image is not None and image.is_visible()

    def add_to_cart_button_is_visible(self, product):
        """Checks if the Add to Cart button is visible within the product element."""
        button = product.query_selector(self.INVENTORY_ITEM_ADD_TO_CART_BUTTON)
        return button is not None and button.is_visible()

    def remove_from_cart_button_is_visible(self, product):
        """Checks if the Remove button is visible within the product element."""
        button = product.query_selector(self.INVENTORY_ITEM_REMOVE_FROM_CART_BUTTON)
        return button is not None and button.is_visible()

    def get_specific_product(self, product_to_add):
        products = self.get_all_products()
        for product in products:
            product_name = (
                product.query_selector(self.INVENTORY_ITEM_NAME).text_content().strip()
            )
            if product_to_add in product_name:
                return product

    def add_product_to_cart(self, product):
        product.query_selector(self.INVENTORY_ITEM_ADD_TO_CART_BUTTON).click()

    def remove_product_from_the_cart(self, product):
        product.query_selector(self.INVENTORY_ITEM_REMOVE_FROM_CART_BUTTON).click()

    def _get_cart_badge(self):
        cart_badge = self.page.locator(self.CART_BADGE)
        return cart_badge

    def cart_badge_is_visible(self):
        return self._get_cart_badge().is_visible()

    def get_cart_items_count(self):
        cart_badge = self._get_cart_badge()
        return int(cart_badge.text_content())
