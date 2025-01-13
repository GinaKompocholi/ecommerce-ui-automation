import logging

from pytest_bdd import parsers, scenarios, then, when

from ui_automation_suite.bdd_tests.page_objects.burger_menu import BurgerMenu
from ui_automation_suite.settings.constants import ABOUT_PAGE

# Link to the feature file
scenarios("../features/burger_menu.feature")


@when(parsers.cfparse("user opens the burger menu"))
def open_burger_menu(burgermenu_page: BurgerMenu):
    burgermenu_page.click_on_burger_menu()
    assert burgermenu_page.burger_menu_is_open(), "Burger menu is not open"
    logging.info("User opened the burger menu")


@then(parsers.cfparse("the menu contains all 4 categories"))
def menu_contains_all_categories(burgermenu_page: BurgerMenu):
    assert burgermenu_page.menu_item_is_displayed(
        "All Items"
    ), "All Items is not displayed"
    assert burgermenu_page.menu_item_is_displayed("About"), "About is not displayed"
    assert burgermenu_page.menu_item_is_displayed("Logout"), "Logout is not displayed"
    assert burgermenu_page.menu_item_is_displayed(
        "Reset App State"
    ), "Reset App State is not displayed"
    logging.info("The menu contains all 4 categories")


@when(parsers.cfparse("user closes the burger menu"))
def close_the_burger_menu(burgermenu_page: BurgerMenu):
    burgermenu_page.close_burger_menu()
    assert not burgermenu_page.burger_menu_is_open(), "Burger menu is still open"
    logging.info("User closed the burger menu")


@when(parsers.cfparse("user selects from menu {menu_item}"))
def navigate_to_burger_menu(menu_item, burgermenu_page: BurgerMenu):
    assert menu_item in [
        "All Items",
        "About",
        "Logout",
        "Reset App State",
    ], f"Invalid menu item: {menu_item}"
    burgermenu_page.select_menu_item(menu_item)
    logging.info(f"User selected {menu_item} from the burger menu")


@then(parsers.cfparse("user is redirected to the about page"))
def redirection_to_about_page(page):
    assert (
        ABOUT_PAGE == page.url
    ), f"Expected to be on the about page, but was on {page.url}"
    logging.info("User was redirected to the about page")
