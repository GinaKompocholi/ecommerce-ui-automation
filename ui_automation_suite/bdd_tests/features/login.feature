@regression @login
Feature: Authentication

  Background:
    Given the login page is displayed

  @login_success @positive
  Scenario: User successfully logs in
    When user tries to login with standard_user
    Then user is redirected to the products page

  @invalid_login @negative
  Scenario Outline: User is unable to login
    When user tries to login with <username>
    Then <error_message> error message is displayed
    And the user remains on the login page

    Examples:
      | username        | error_message |
      | locked_out_user | locked out    |
      | wrong_username  | invalid creds |

  @missing_credentials @negative
  Scenario Outline: User can't log in without providing both username and password
    When user tries to login without <credential>
    Then <error_message> error message is displayed
    And the user remains on the login page

    Examples:
      | credential | error_message    |
      | username   | missing username |
      | password   | missing password |

  # Expected: User logs in within acceptable time limits.
  # Actual: Login takes too long with performance_glitch_user.
  @performance_glitch_user @bug
  Scenario: [BUG] User tries to login but it takes too long
    When user tries to login with performance_glitch_user
    Then user is redirected to the products page

  # TODO: Add a visual test to verify button alignment on the products page.
