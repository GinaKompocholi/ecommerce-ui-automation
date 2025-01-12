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

  # FAILS as there is a bug in the website
  @burgermenu_reset_app_state
  Scenario: User resets app state and the site returns to initial stage
    When user adds product Backpack to the cart
    Then the cart icon displays 1 product(s)
    When user opens the burger menu
    And user selects from menu Reset App State
    Then the cart icon displays 0 product(s)
    And all products are fully visible with all attributes

  #TODO: Reset App State is not working as expected, so the test fails
  @burgermenu_in_shopping_cart
  Scenario: User opens burger menu in shopping cart
    When user navigates to the shopping cart
    Then burger menu button is visible and menu is closed
    When user opens the burger menu
    And user selects from menu Reset App State
    Then the cart icon displays 0 product(s)
    Then cart is empty
