@regression @burgermenu
Feature: Burgermenu navigation

  Background:
    Given the login page is displayed
    When user tries to login with standard_user
    Then user is redirected to the products page
    Then burger menu button is visible and menu is closed

  @burgermenu_logout @burgermenu_about
  Scenario: User chooses Logout and About from burger menu
    When user opens the burger menu
    And user selects from menu Logout
    Then user is redirected to the login page
    When user tries to login with standard_user
    Then user is redirected to the products page
    When user opens the burger menu
    And user selects from menu About
    Then user is redirected to the about page

  @burgermenu_all_items
  Scenario: User chooses All Items from burger menu
    When user views product details for product Backpack
    Then user is redirected to the product details page
    When user opens the burger menu
    And user selects from menu All Items
    Then user is redirected to the products page

  @burgermenu_open_close
  Scenario: User opens and closes burger menu
    When user opens the burger menu
    And user closes the burger menu
    Then burger menu button is visible and menu is closed

  @burgermenu_in_shopping_cart @burgermenu_in_checkout
  Scenario: User opens burger menu in shopping cart and checkout
    When user navigates to the shopping cart
    Then burger menu button is visible and menu is closed
    When user opens the burger menu
    Then the menu contains all 4 categories
    When user closes the burger menu
    Then burger menu button is visible and menu is closed
    When user proceeds to checkout
    And user opens the burger menu
    Then the menu contains all 4 categories
    When user closes the burger menu
    Then burger menu button is visible and menu is closed

  # Expected: Resetting the app state reverts all buttons to their default state (Add to cart).
  # Actual: Buttons remain in their modified state after resetting the app state.
  @burgermenu_reset_app_state @bug
  Scenario: [BUG] User resets app state
    When user adds product Backpack to the cart
    Then the cart icon displays 1 product(s)
    When user opens the burger menu
    And user selects from menu Reset App State
    Then the cart icon displays 0 product(s)
    And all products are fully visible with all attributes
