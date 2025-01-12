from ui_automation_suite.bdd_tests.page_objects.base_page import BasePage


class LoginPage(BasePage):
    # LOCATORS
    LOGIN_CONTAINER = "[data-test='login-container']"
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    CREDENTIALS_CONTAINER = "[data-test='login-credentials-container']"
    ERROR_MESSAGE = "[data-test='error']"
    ERROR_BUTTON = "[data-test='error-button']"

    def navigate(self, url):
        """Navigate to the login page."""
        self.page.goto(url)

    def login_container_is_displayed(self):
        """Check if the login container is displayed."""
        return self.page.is_visible(self.LOGIN_CONTAINER)

    def username_field_is_displayed(self):
        """Check if the username field is displayed."""
        return self.page.is_visible(self.USERNAME_INPUT)

    def password_field_is_displayed(self):
        """Check if the password field is displayed."""
        return self.page.is_visible(self.PASSWORD_INPUT)

    def login_button_is_displayed(self):
        """Check if the login button is displayed."""
        return self.page.is_visible(self.LOGIN_BUTTON)

    def credentials_container_is_displayed(self):
        """Check if the credentials container is displayed."""
        return self.page.is_visible(self.CREDENTIALS_CONTAINER)

    def error_message_is_displayed(self):
        """Check if the error message is displayed."""
        return self.page.is_visible(self.ERROR_MESSAGE)

    def error_button_is_displayed(self):
        """Check if the error message is displayed."""
        return self.page.is_visible(self.ERROR_BUTTON)

    def fill_login_credentials(self, username, password):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.page.click(self.LOGIN_BUTTON)

    def get_displayed_error_message(self):
        return self.page.text_content(self.ERROR_MESSAGE)
