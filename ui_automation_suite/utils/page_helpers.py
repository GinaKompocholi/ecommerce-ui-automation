from ui_automation_suite.bdd_tests.page_objects.checkout_page import CheckoutPage
from ui_automation_suite.bdd_tests.page_objects.shopping_cart_page import (
    ShoppingCartPage,
)
from ui_automation_suite.settings.constants import AVAILABLE_PRODUCTS, INVALID_PRODUCT


def validate_product_name(product_name: str):
    """
    Validate that the product name exists in AVAILABLE_PRODUCTS.

    Args:
        product_name (str): Name of the product to validate.

    Raises:
        AssertionError: If the product name is invalid.
    """
    assert product_name in AVAILABLE_PRODUCTS, INVALID_PRODUCT


def get_page_object(page_name: str, page):
    """
    Get the page object corresponding to the specified page name.

    Args:
        page_name (str): Name of the page (e.g., "Shopping Cart", "Checkout").
        page: Playwright page instance.

    Returns:
        Page object corresponding to the specified page.
    """
    if page_name.lower() == "shopping cart":
        return ShoppingCartPage(page)
    elif page_name.lower() == "checkout":
        return CheckoutPage(page)
    else:
        raise ValueError(f"Unknown page name: {page_name.lower()}")
