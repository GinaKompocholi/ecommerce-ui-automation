@regression @checkout
Feature: Checkout

  Background:
    Given the login page is displayed
    When user tries to login with standard_user
    Then user is redirected to the products page
    When user adds product Onesie to the cart
    And user navigates to the shopping cart
    Then the cart icon displays 1 product(s)
    When user proceeds to checkout
    Then user lands on checkout Information

  @checkout_information @initial_state_validated @cancel_checkout_information
  Scenario: Checkout Information - initial state validated & cancel checkout
    When user clicks on shopping cart icon
    Then user is redirected to the shopping cart page
    When user proceeds to checkout
    Then the cart icon displays 1 product(s)
    When user clicks on Cancel
    Then user is redirected to the products page

  @mandatory_fields_required
  Scenario: Checkout mandatory fields are required
    When user clicks on Continue
    Then error message 'First Name is required' is displayed
    When user fills in First Name
    When user clicks on Continue
    Then error message 'Last Name is required' is displayed
    And user fills in Last Name
    When user clicks on Continue
    And user fills in Postal Code
    Then error message 'Postal Code is required' is displayed

  @checkout_overview @initial_state_validated @cancel_checkout_overview
  Scenario: Checkout Overview - initial state validated & cancel checkout
    When user fills in First Name
    And user fills in Last Name
    And user fills in Postal Code
    And user clicks on Continue
    Then user lands on checkout Overview
    And the checkout contains 1 product(s)
    And product Onesie is displayed in the Checkout
    And the quantity of product Onesie is 1 in the Checkout
    And the price of product Onesie is $7.99 in the Checkout
    And the full name of product Onesie displayed is Sauce Labs Onesie in the Checkout
    When user clicks on Cancel
    Then user is redirected to the products page
