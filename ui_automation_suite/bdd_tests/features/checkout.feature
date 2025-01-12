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


  @checkout_validated
  Scenario: Checkout initial state validated
