import logging
from typing import Union

from pytest_bdd import given, parsers, then, when

from ui_automation_suite.bdd_tests.page_objects.checkout_page import CheckoutPage
from ui_automation_suite.bdd_tests.page_objects.login_page import LoginPage
from ui_automation_suite.bdd_tests.page_objects.products_page import ProductPage
from ui_automation_suite.bdd_tests.page_objects.shopping_cart_page import (
    ShoppingCartPage,
)
from ui_automation_suite.bdd_tests.page_objects.sidebar import BurgerMenu
from ui_automation_suite.settings.config import AppEnvSettings
from ui_automation_suite.settings.constants import (
    ALL_PRODUCTS_PAGE,
    BASE_URL,
    PRODUCT_DETAILS_PAGE,
    SHOPPING_CART_PAGE,
)
from ui_automation_suite.utils.page_helpers import (
    get_page_object,
    validate_product_name,
)


def validate_standard_login_page_elements(page, login_page: LoginPage):
    assert page.url == BASE_URL, f"Unexpected URL: {page.url}"
    assert login_page.login_container_is_displayed(), "Login container is not displayed"
    assert login_page.username_field_is_displayed(), "Username field is not displayed"
    assert login_page.password_field_is_displayed(), "Password field is not displayed"
    assert login_page.login_button_is_displayed(), "Login button is not displayed"
    assert (
        login_page.credentials_container_is_displayed()
    ), "Credentials container is not displayed"


@given(parsers.cfparse("the login page is displayed"))
def login_page_is_displayed(page, login_page: LoginPage):
    login_page.navigate(BASE_URL)
    validate_standard_login_page_elements(page, login_page)
    assert (
        not login_page.error_message_is_displayed()
    ), "Error message is unexpectedly displayed"
    logging.info("Login page is displayed")


@then(parsers.cfparse("user is redirected to the login page"))
def redirection_to_login_page(page, login_page: LoginPage):
    validate_standard_login_page_elements(page, login_page)
    logging.info("User was redirected to the login page")


@when(parsers.cfparse("user tries to login with {username_type}"))
def login_with_specific_role(
    username_type, login_page: LoginPage, app_env_settings: AppEnvSettings
):
    username = app_env_settings.get_username(username_type)
    if username is None:
        raise ValueError(f"Invalid username type: {username_type}")
    login_page.fill_login_credentials(username, app_env_settings.password)
    login_page.click_login_button()


@then(parsers.cfparse("user is redirected to the products page"))
def redirection_to_homepage(page):
    assert (
        ALL_PRODUCTS_PAGE in page.url
    ), f"Expected to be on the products page, but was on {page.url}"
    logging.info("User was redirected to the products page")


@then(parsers.cfparse("all products are fully visible with all attributes"))
def products_are_displayed(page, product_page: ProductPage):
    products_displayed = product_page.get_all_products()
    assert len(products_displayed) > 0, "No products were displayed"
    logging.info(
        f"Validation started: {len(products_displayed)} product(s) found on the page."
    )

    for product in products_displayed:
        assert product_page.name_is_visible(product), "Product name is missing"
        product_name = product_page.get_product_name(product)
        assert product_page.image_is_visible(
            product
        ), f"Product {product_name} image is missing"
        assert product_page.description_is_visible(
            product
        ), f"Product {product_name}  description is missing"
        assert product_page.price_is_visible(
            product
        ), f"Product {product_name}  price is missing"
        assert product_page.add_to_cart_button_is_visible(
            product
        ), f"Product '{product_name}' button [Add to Cart] is missing"
        logging.debug(f"Product '{product_name}' is fully visible")
    logging.info("All products are fully visible with all attributes")


@when(parsers.cfparse("user adds product {product_name} to the cart"))
def add_product_to_cart(product_name, product_page: ProductPage):
    validate_product_name(product_name)

    all_products = product_page.get_all_products()
    assert all_products, "No products were displayed"
    product = product_page.get_specific_product(product_name, all_products)
    product_page.add_product_to_cart(product)
    # Validate product is added to the cart
    assert not product_page.add_to_cart_button_is_visible(
        product
    ), "Add to Cart button is still visible"
    assert product_page.remove_from_cart_button_is_visible(
        product
    ), "Remove button is not visible"
    logging.info(f"{product_name} was added to the cart")


@then(parsers.cfparse("the cart icon displays {total_products:d} product(s)"))
def product_is_added_to_cart(total_products: int, product_page: ProductPage):
    if total_products == 0:
        assert not product_page.cart_badge_is_visible(), "Cart badge is visible"
        logging.info("The cart displays no item(s), reflecting the correct total.")
    else:
        # Validate the badge is visible
        assert (
            product_page.cart_badge_is_visible()
        ), "Cart badge is not visible after adding an item"

        # Validate the cart badge text updates to total_products
        cart_counter = product_page.get_cart_items_count()
        assert cart_counter == int(
            total_products
        ), f"Expected cart to have {total_products} product(s), but got {cart_counter}"
        logging.info(
            f"The cart displays {total_products} item(s), reflecting the correct total."
        )


@then(parsers.cfparse("burger menu button is visible and menu is closed"))
def navigate_to_burger_menu(burgermenu_page: BurgerMenu):
    assert burgermenu_page.menu_button_is_displayed(), "Burger menu is not displayed"
    assert not burgermenu_page.burger_menu_is_open(), "Burger menu is open"
    logging.info("burger menu button is visible and menu is closed")


@when(parsers.cfparse("user views product details for product {product_name}"))
def view_product_details(product_name, product_page: ProductPage):
    validate_product_name(product_name)
    all_products = product_page.get_all_products()
    assert all_products, "No products were displayed"
    product = product_page.get_specific_product(product_name, all_products)
    product_page.click_on_product_name(product)


@then(parsers.cfparse("user is redirected to the product details page"))
def redirection_to_product_details_page(page):
    assert (
        PRODUCT_DETAILS_PAGE in page.url
    ), f"Expected to be on the product details page, but was on {page.url}"
    logging.info("User was redirected to the products details page")


@then(parsers.cfparse("user is redirected to the shopping cart page"))
def redirection_to_shopping_cart_page(page):
    assert (
        SHOPPING_CART_PAGE in page.url
    ), f"Expected to be on the shopping cart page, but was on {page.url}"
    logging.info("User was redirected to the shopping cart page")


@when(parsers.cfparse("user navigates to the shopping cart"))
def proceed_to_shopping_cart(shopping_cart_page: ShoppingCartPage):
    shopping_cart_page.click_on_shopping_cart()
    assert (
        shopping_cart_page.shopping_cart_is_displayed()
    ), "Shopping cart is not displayed"
    logging.info("User proceeds to the cart")


@when(parsers.cfparse("user proceeds to checkout"))
def proceed_to_checkout(shopping_cart_page: ShoppingCartPage):
    shopping_cart_page.click_checkout()
    logging.info("User proceeded to checkout")


@then(parsers.cfparse("the {page_name} contains {cart_items_count:d} product(s)"))
def cart_contains_products(page_name: str, cart_items_count: int, page):
    # Declare the type of page_obj as a union of possible page types
    page_obj: Union[ShoppingCartPage, CheckoutPage]

    # Dynamically instantiate the correct page
    if page_name.lower() == "shopping cart":
        page_obj = ShoppingCartPage(page)
    elif page_name.lower() == "checkout":
        page_obj = CheckoutPage(page)
    else:
        raise ValueError(f"Unknown page name: {page_name.lower()}")

    # Use the cart_list component to validate
    cart_list = page_obj.cart_list

    total_cart_items = len(cart_list.get_all_cart_products())
    assert (
        total_cart_items == cart_items_count
    ), f"Expected {cart_items_count} products, but got {total_cart_items}"
    logging.info(f"The {page_name} contains {cart_items_count:d} product(s)")


# Then product Bike Light is displayed in the Shopping Cart
# Then product Bike Light is displayed in the Checkout
@then(parsers.cfparse("product {product_name} is displayed in the {page_name}"))
def product_is_displayed_in_cart(product_name: str, page_name: str, page):
    # Validate the product name explicitly
    validate_product_name(product_name)
    # Get the page object
    page_obj = get_page_object(page_name, page)

    # Use the cart_list component to validate
    cart_list = page_obj.cart_list

    all_products = cart_list.get_all_cart_products()
    assert all_products, "No products were displayed"
    product = cart_list.get_specific_product(product_name, all_products)
    assert cart_list.product_name_is_visible(product), "Product name is not displayed"
    logging.info(f"Product {product_name} is displayed in the {page_name}")


@then(
    parsers.cfparse(
        "the quantity of product {product_name} is {quantity:d} in the {page_name}"
    )
)
def product_quantity_in_cart(product_name: str, quantity: int, page_name: str, page):
    # Validate the product name explicitly
    validate_product_name(product_name)
    # Get the page object
    page_obj = get_page_object(page_name, page)

    all_products = page_obj.cart_list.get_all_cart_products()
    assert all_products, "No products were displayed"
    product = page_obj.cart_list.get_specific_product(product_name, all_products)
    product_quantity_in_cart = page_obj.cart_list.get_product_quantity(product)
    assert (
        product_quantity_in_cart == quantity
    ), f"Unexpected quantity of product in the {page_name}"
    logging.info(
        f"Product {product_name} quantity displayed in {page_name} is as expected."
    )


@then(
    parsers.cfparse("the price of product {product_name} is {price} in the {page_name}")
)
def product_price_in_cart(product_name: str, price: str, page_name: str, page):
    # Validate the product name explicitly
    validate_product_name(product_name)
    # Get the page object
    page_obj = get_page_object(page_name, page)

    all_products = page_obj.cart_list.get_all_cart_products()
    assert all_products, "No products were displayed"
    product = page_obj.cart_list.get_specific_product(product_name, all_products)
    actual_price = page_obj.cart_list.get_product_price(product)
    expected_price = float(price.replace("$", ""))
    assert actual_price == expected_price, (
        f"Expected price for product {product_name} is ${expected_price} "
        f"but the displayed price is ${actual_price}"
    )
    logging.info(
        f"Product {product_name} price displayed in {page_name} is as expected."
    )


@then(parsers.cfparse("user can remove product {product_name} from the {page_name}"))
def user_can_remove_product_from_cart(product_name: str, page_name: str, page):
    # Validate the product name explicitly
    validate_product_name(product_name)
    # Get the page object
    page_obj = get_page_object(page_name, page)

    all_products = page_obj.cart_list.get_all_cart_products()
    assert all_products, "No products were displayed"
    product = page_obj.cart_list.get_specific_product(product_name, all_products)
    assert page_obj.cart_list.remove_product_button_is_visible(
        product
    ), f"Product {product_name} cannot be removed from the {page_name}"
    logging.info(f"User can remove product {product_name} from the {page_name}")


@when(parsers.cfparse("user removes product {product_name} from the {page_name}"))
def user_removes_product_from_cart(product_name: str, page_name: str, page):
    # Validate the product name explicitly
    validate_product_name(product_name)
    # Get the page object
    page_obj = get_page_object(page_name, page)

    all_products = page_obj.cart_list.get_all_cart_products()
    assert all_products, "No products were displayed"
    product = page_obj.cart_list.get_specific_product(product_name, all_products)
    page_obj.cart_list.remove_product_from_the_cart(product)
    logging.info(f"User removed product {product_name} from the {page_name}")


@then(
    parsers.cfparse(
        "the full name of product {product_name} displayed is "
        "{product_full_name} in the {page_name}"
    )
)
def product_name_in_cart(
    product_name: str, product_full_name: str, page_name: str, page
):
    # Validate the product name explicitly
    validate_product_name(product_name)
    # Get the page object
    page_obj = get_page_object(page_name, page)

    # Validate product full name
    all_products = page_obj.cart_list.get_all_cart_products()
    assert all_products, "No products were displayed"
    product = page_obj.cart_list.get_specific_product(product_name, all_products)
    actual_name = page_obj.cart_list.get_product_name(product)
    assert actual_name == product_full_name, (
        f"Expected name for product {product_name} is '{product_full_name}' "
        f"but the displayed name is '{actual_name}'"
    )
    logging.info(
        f"The name of product {product_name} in the {page_name} is '{actual_name}'"
    )
