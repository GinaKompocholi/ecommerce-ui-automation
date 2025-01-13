from ui_automation_suite.bdd_tests.page_objects.base_page import BasePage


class BurgerMenu(BasePage):
    # LOCATORS
    MENU_BUTTON = "[id='react-burger-menu-btn']"
    MENU = "[class='bm-menu-wrap']"
    ALL_ITEMS = "[data-test='inventory-sidebar-link']"
    ABOUT = "[data-test='about-sidebar-link']"
    LOGOUT = "[data-test='logout-sidebar-link']"
    RESET_APP_STATE = "[data-test='reset-sidebar-link']"
    CROSS_BUTTON = "[id='react-burger-cross-btn']"

    MENU_ITEMS = {
        "All Items": ALL_ITEMS,
        "About": ABOUT,
        "Logout": LOGOUT,
        "Reset App State": RESET_APP_STATE,
    }

    def click_on_burger_menu(self):
        self.page.click(self.MENU_BUTTON)

    def menu_button_is_displayed(self):
        return self.page.is_visible(self.MENU_BUTTON)

    def burger_menu_is_open(self):
        return self.page.is_visible(self.MENU)

    def select_menu_item(self, menu_item):
        self.page.click(self.MENU_ITEMS[menu_item])

    def menu_item_is_displayed(self, menu_item):
        return self.page.is_visible(self.MENU_ITEMS[menu_item])

    def close_burger_menu(self):
        self.page.click(self.CROSS_BUTTON)
