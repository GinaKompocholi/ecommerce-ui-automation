import logging

from pytest_bdd import parsers, scenarios, then, when

from ui_automation_suite.bdd_tests.page_objects.login_page import LoginPage

# Link to the feature file
from ui_automation_suite.settings.config import AppEnvSettings
from ui_automation_suite.settings.constants import BASE_URL

scenarios("../features/login.feature")


def validate_standard_homepage_elements(page, login_page: LoginPage):
    assert page.url == BASE_URL, f"Unexpected URL: {page.url}"
    assert login_page.login_container_is_displayed(), "Login container is not displayed"
    assert login_page.username_field_is_displayed(), "Username field is not displayed"
    assert login_page.password_field_is_displayed(), "Password field is not displayed"
    assert login_page.login_button_is_displayed(), "Login button is not displayed"
    assert (
        login_page.credentials_container_is_displayed()
    ), "Credentials container is not displayed"


@when(parsers.cfparse("user tries to login without {credential_missing}"))
def login_with_missing_password(
    credential_missing, login_page: LoginPage, app_env_settings: AppEnvSettings
):
    if credential_missing == "username":
        login_page.fill_login_credentials("", app_env_settings.password)
    else:
        login_page.fill_login_credentials(
            app_env_settings.get_username("standard_user"), ""
        )
    login_page.click_login_button()


@then(parsers.cfparse("{errortype} error message is displayed"))
def products_are_displayed(errortype, page, login_page: LoginPage):
    assert errortype in [
        "locked out",
        "invalid creds",
        "missing username",
        "missing password",
    ], "Invalid error type"

    assert login_page.error_message_is_displayed(), "Error message is not displayed"
    assert login_page.error_button_is_displayed(), "Error button is not displayed"

    error_messages = {
        "locked out": "Sorry, this user has been locked out.",
        "invalid creds": "Username and password do not match any user in this service",
        "missing username": "Username is required",
        "missing password": "Password is required",
    }

    expected_error_message = error_messages[errortype]

    displayed_error_msg = login_page.get_displayed_error_message()
    assert (
        displayed_error_msg == f"Epic sadface: {expected_error_message}"
    ), "Error message is not as expected."
    logging.info("User sees an error message")


@then(parsers.cfparse("the user remains on the login page"))
def user_remains_on_login_page(page, login_page: LoginPage):
    validate_standard_homepage_elements(page, login_page)
    logging.info("User remains on the login page")
