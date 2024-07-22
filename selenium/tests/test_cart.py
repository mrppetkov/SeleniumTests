from pytest import mark
from selenium.webdriver.common.by import By


@mark.browser
def test_add_to_cart_render(
    logged_in_driver_homepage,
    config,
):
    backpack_add_to_cart_button = logged_in_driver_homepage.find_element(By.ID, config["backpack_add_to_cart_button"])  #noqa: E501
    assert backpack_add_to_cart_button.is_displayed() and backpack_add_to_cart_button.is_enabled(), "Add to cart button is not visible or interactive."  #noqa: E501
    assert backpack_add_to_cart_button.text.strip() == "Add to cart", f"Expected 'Add to cart' button text, but found '{backpack_add_to_cart_button.text.strip()}'"  #noqa: E501


@mark.browser
@mark.smoke
def test_add_to_cart_click(
    logged_in_with_item_in_cart,
    config,
):
    shopping_cart = logged_in_with_item_in_cart.find_element(By.CLASS_NAME, config["shopping_cart_badge"])  #noqa: E501
    assert int(shopping_cart.text) == 1


@mark.browser
def test_cart_contains_backpack(logged_in_with_item_in_cart):
    item_name_elements = logged_in_with_item_in_cart.find_elements(By.CLASS_NAME, "inventory_item_name")  #noqa: E501

    item_names = [item.text for item in item_name_elements]
    
    expected_item_name = "Sauce Labs Backpack"
    assert expected_item_name in item_names, f"{expected_item_name} should be present in the cart."  #noqa: E501


@mark.browser
def test_shopping_items_render(
    logged_in_driver_homepage,
    config,
):
    shopping_cart_elements = logged_in_driver_homepage.find_elements(By.CLASS_NAME, config["shopping_cart_badge"])  #noqa: E501
    assert len(shopping_cart_elements) == 0, "The shopping cart badge should not be present on the page."  #noqa: E501
