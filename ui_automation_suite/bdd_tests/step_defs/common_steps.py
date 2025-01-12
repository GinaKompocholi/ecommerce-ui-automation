import logging

from pytest_bdd import given, parsers, then, when

from ui_automation_suite.bdd_tests.page_objects.login_page import LoginPage
from ui_automation_suite.bdd_tests.page_objects.products_page import ProductPage
from ui_automation_suite.bdd_tests.page_objects.shopping_cart_page import (
    ShoppingCartPage,
)
from ui_automation_suite.bdd_tests.page_objects.sidebar import BurgerMenu
from ui_automation_suite.settings.config import AppEnvSettings
from ui_automation_suite.settings.constants import (
    ALL_PRODUCTS_PAGE,
    AVAILABLE_PRODUCTS,
    BASE_URL,
    INVALID_PRODUCT,
    PRODUCT_DETAILS_PAGE,
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
    assert product_name in AVAILABLE_PRODUCTS, INVALID_PRODUCT
    product = product_page.get_specific_product(product_name)
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
    assert product_name in AVAILABLE_PRODUCTS, INVALID_PRODUCT
    product = product_page.get_specific_product(product_name)
    product_page.click_on_product_name(product)


@then(parsers.cfparse("user is redirected to the product details page"))
def redirection_to_product_details_page(page):
    assert (
        PRODUCT_DETAILS_PAGE in page.url
    ), f"Expected to be on the products page, but was on {page.url}"
    logging.info("User was redirected to the products details page")


@when(parsers.cfparse("user navigates to the shopping cart"))
def proceed_to_shopping_cart(shopping_cart_page: ShoppingCartPage):
    shopping_cart_page.click_on_shopping_cart()
    assert (
        shopping_cart_page.shopping_cart_is_displayed()
    ), "Shopping cart is not displayed"
    logging.info("User proceeds to the cart")
