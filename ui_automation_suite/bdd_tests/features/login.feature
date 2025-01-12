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
      | username        | error_message       |
      | locked_out_user | locked out          |
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

#  TODO: Add performance test
#  @performance_glitch_user
#  Scenario: User can't log in without providing password
#    When user tries to login with username performance_glitch_user and password secret_sauce
#    Then user is redirected to the products page
