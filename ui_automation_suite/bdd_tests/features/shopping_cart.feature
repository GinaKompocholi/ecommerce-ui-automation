@regression @shopping_cart
Feature: Shopping cart

  Background:
    Given the login page is displayed
    When user tries to login with standard_user
    Then user is redirected to the products page

  # FAILS as user should not be able to proceed to checkout with an empty cart
  @shopping_cart_initial_state @empty_cart @fails
  Scenario: Verify the initial state of an empty shopping cart
    When user navigates to the shopping cart
    Then the cart icon displays 0 product(s)
    Then the cart contains 0 product(s)
    And user can continue shopping
    And user can't proceed to first checkout step

  @shopping_cart_product_validated
  Scenario: Shopping cart with one product
    When user adds product Bike Light to the cart
    And user navigates to the shopping cart
    Then the cart icon displays 1 product(s)
    And the shopping cart contains 1 product(s)
    And product Bike Light is displayed in the Shopping cart
    And the full name of product Bike Light displayed is Sauce Labs Bike Light in the Shopping cart
    And the quantity of product Bike Light is 1 in the Shopping cart
    And the price of product Bike Light is $9.99 in the Shopping cart
    And user can remove product Bike Light from the cart
    And user can continue shopping
    And user can proceed to first checkout step

  @shopping_continue_shopping @shopping_cart_remove_product
  Scenario: User continues shopping, adds and removes product from the cart
    When user adds product Bike Light to the cart
    And user navigates to the shopping cart
    When user continues shopping
    Then user is redirected to the products page
    When user adds product Bolt T-Shirt to the cart
    And user navigates to the shopping cart
    Then the cart icon displays 2 product(s)
    When user removes product Bolt T-Shirt from the shopping cart
    Then the cart icon displays 1 product(s)
    And the cart contains 1 product(s)
