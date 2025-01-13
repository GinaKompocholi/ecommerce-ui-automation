import logging

from pytest_bdd import parsers, scenarios, then, when

from ui_automation_suite.bdd_tests.page_objects.products_page import ProductPage
from ui_automation_suite.settings.constants import AVAILABLE_PRODUCTS, INVALID_PRODUCT

# Link to the feature file
scenarios("../features/products.feature")

NAME_ASC = "ascending name"
NAME_DESC = "descending name"
PRICE_ASC = "ascending price"
PRICE_DESC = "descending price"


@when(parsers.cfparse("user sorts products in {order_type} order {description}"))
def sort_products(order_type, description, product_page: ProductPage):
    assert order_type in [
        NAME_ASC,
        NAME_DESC,
        PRICE_ASC,
        PRICE_DESC,
    ], "Invalid order type"
    product_page.sort_products_by_order(order_type)
    logging.info(f"Products were sorted in {order_type} {description} order")


@then(parsers.cfparse("products are displayed in {order_type} order {description}"))
def products_displayed_sorted(order_type, description, product_page: ProductPage):
    assert order_type in [
        NAME_ASC,
        NAME_DESC,
        PRICE_ASC,
        PRICE_DESC,
    ], "Invalid order type"

    # numerical order: descending price, ascending price
    if "price" in order_type:
        actual_sorted_results = product_page.get_sorted_product_prices()
    # alphabetical order: a to z(ascending), z to a(descending)
    else:
        actual_sorted_results = product_page.get_sorted_product_names()

    # Determine sorting order
    reverse = order_type in [NAME_DESC, PRICE_DESC]

    # Validate the sorting
    expected_sorted_results = sorted(actual_sorted_results, reverse=reverse)
    assert (
        actual_sorted_results == expected_sorted_results
    ), f"Products are not sorted in {order_type} order"
    logging.info(f"Products are correctly sorted in {order_type} order {description}")


@when(
    parsers.cfparse(
        "user removes product {product_name} from the cart on the product list"
    )
)
def removed_product_from_cart(product_name, product_page: ProductPage):
    assert product_name in AVAILABLE_PRODUCTS, INVALID_PRODUCT
    all_products = product_page.get_all_products()
    assert all_products, "No products were displayed"
    product = product_page.get_specific_product(product_name, all_products)
    product_page.remove_product_from_the_cart(product)
    # Validate product is removed from the cart
    assert product_page.add_to_cart_button_is_visible(product), (
        f"{product_name} wasn't removed from the cart as "
        f"[Add to Cart] button isn't visible"
    )
