from ui_automation_suite.bdd_tests.page_objects.base_page import BasePage


class BurgerMenu(BasePage):
    # LOCATORS
    MENU_BUTTON = "[id='react-burger-menu-btn']"
    MENU = "[class='bm-menu-wrap']"
    ALL_ITEMS = "[data-test='inventory-sidebar-link']"
    ABOUT = "[data-test='about-sidebar-link']"
    LOGOUT = "[data-test='logout-sidebar-link']"
    RESET_APP_STATE = "[data-test='reset-sidebar-link']"
    CLOSE_BURGER_MENU = "[id='react-burger-cross-btn']"

    def click_on_burger_menu(self):
        self.page.click(self.MENU_BUTTON)

    def menu_button_is_displayed(self):
        return self.page.is_visible(self.MENU_BUTTON)

    def burger_menu_is_open(self):
        return self.page.is_visible(self.MENU)

    def select_menu_item(self, menu_item):
        menu_items = {
            "All Items": self.ALL_ITEMS,
            "About": self.ABOUT,
            "Logout": self.LOGOUT,
            "Reset App State": self.RESET_APP_STATE,
        }
        self.page.click(menu_items[menu_item])

    def close_burger_menu(self):
        self.page.click(self.CLOSE_BURGER_MENU)
