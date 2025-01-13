@regression @products
Feature: Products page

  Background:
    Given the login page is displayed
    When user tries to login with standard_user
    Then user is redirected to the products page

  @products_initial_state
  Scenario: Initial state of products page
    Then all products are fully visible with all attributes
    And products are displayed in ascending name order (A to Z)
    And the cart icon displays 0 product(s)
    And burger menu button is visible and menu is closed

  @products_sorted_by_name @sort_products
  Scenario: User can sort products by name
    When user sorts products in ascending name order (A to Z)
    Then products are displayed in ascending name order (A to Z)
    When user sorts products in descending name order (Z to A)
    Then products are displayed in descending name order (Z to A)

  @products_sorted_by_price @sort_products
  Scenario: User can sort products by price
    When user sorts products in descending price order (high to low)
    Then products are displayed in descending price order (high to low)
    When user sorts products in ascending price order (low to high)
    Then products are displayed in ascending price order (low to high)

  @product_added_to_cart @product_removed_from_cart
  Scenario: User adds and removes products from cart
    When user adds product Bike Light to the cart
    Then the cart icon displays 1 product(s)
    When user removes product Bike Light from the cart on the product list
    Then the cart icon displays 0 product(s)
    When user adds product Test.allTheThings() T-Shirt (Red) to the cart
    When user adds product Onesie to the cart
    Then the cart icon displays 2 product(s)

  @product_details_page
  Scenario: User views product details
    When user views product details for product Backpack
    Then user is redirected to the product details page
