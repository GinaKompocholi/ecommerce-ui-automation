from ui_automation_suite.bdd_tests.page_objects.base_page import BasePage


class CheckoutPage(BasePage):
    # LOCATORS
    # checkout-step-one: Your Information
    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-test='lastName']"
    POSTAL_CODE = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"
    # checkout-step-two: Overview
    TITLE = "[data-test='title']"
    CART_LIST = "[data-test='cart-list']"
    INVENTORY_ITEM = "[data-test='inventory-item']"
    PAYMENT_INFO_LABEL = "[data-test='payment-info-label']"
    PAYMENT_INFO_VALUE = "[data-test='payment-info-value']"
    SHIPPING_INFO_VALUE = "[data-test='shipping-info-value']"
    TOTAL_INFO_LABEL = "[data-test='total-info-label']"
    SUBTOTAL_LABEL = "[data-test='subtotal-label']"
    TAX_LABEL = "[data-test='tax-label']"
    TOTAL_LABEL = "[data-test='total-label']"
    FINISH_BUTTON = "[data-test='finish']"
    CHECKOUT_COMPLETE_CONTAINER = "[data-test='checkout-complete-container']"
    PONY_EXPRESS = "[data-test='pony-express']"
    COMPLETE_HEADER = "[data-test='complete-header']"
    COMPLETE_TEXT = "[data-test='complete-text']"
    BACK_TO_PRODUCTS_BUTTON = "[data-test='back-to-products']"
