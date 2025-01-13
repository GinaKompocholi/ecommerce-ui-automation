@regression @products
Feature: Products page

  Background:
    Given the login page is displayed

  @products_initial_state
  Scenario: Initial state of products page
    When user tries to login with standard_user
    Then user is redirected to the products page
    Then all products are fully visible with all attributes
    And products are displayed in ascending name order (A to Z)
    And the cart icon displays 0 product(s)
    And burger menu button is visible and menu is closed

  @products_sorted_by_name @sort_products
  Scenario: User can sort products by name
    When user tries to login with standard_user
    Then user is redirected to the products page
    When user sorts products in ascending name order (A to Z)
    Then products are displayed in ascending name order (A to Z)
    When user sorts products in descending name order (Z to A)
    Then products are displayed in descending name order (Z to A)

  @products_sorted_by_price @sort_products
  Scenario: User can sort products by price
    When user tries to login with standard_user
    Then user is redirected to the products page
    When user sorts products in descending price order (high to low)
    Then products are displayed in descending price order (high to low)
    When user sorts products in ascending price order (low to high)
    Then products are displayed in ascending price order (low to high)

  @product_added_to_cart @product_removed_from_cart
  Scenario: User adds and removes products from cart
    When user tries to login with standard_user
    Then user is redirected to the products page
    When user adds product Bike Light to the cart
    Then the cart icon displays 1 product(s)
    When user removes product Bike Light from the cart on the product list
    Then the cart icon displays 0 product(s)
    When user adds product Test.allTheThings() T-Shirt (Red) to the cart
    When user adds product Onesie to the cart
    Then the cart icon displays 2 product(s)

  # Expected: All selected products should be added to the cart.
  # Actual: Products Bolt T-Shirt and Fleece Jacket can't be added to the cart.
  @problem_user @problem_user_add_product @bug
  Scenario: [BUG] User is able to add products to the cart
    When user tries to login with problem_user
    Then user is redirected to the products page
    And all products are fully visible with all attributes
    When user adds product Bike Light to the cart
    And user adds product Backpack to the cart
    And user adds product Onesie to the cart
    And user adds product Bolt T-Shirt to the cart
    And user adds product Fleece Jacket to the cart
    And user adds product Test.allTheThings() T-Shirt (Red) to the cart

  # Expected: Products removed from the cart should no longer appear in it.
  # Actual: Product Bike Light can't be removed
  @problem_user @problem_user_remove_product @bug
  Scenario: [BUG] User is able to remove product from the cart
    When user tries to login with problem_user
    Then user is redirected to the products page
    And all products are fully visible with all attributes
    When user adds product Bike Light to the cart
    And user removes product Bike Light from the cart on the product list

  @product_details_page
  Scenario: User views product details
    When user tries to login with standard_user
    Then user is redirected to the products page
    When user views product details for product Backpack
    Then user is redirected to the product details page
