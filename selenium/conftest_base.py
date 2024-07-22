from pytest import fixture
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from configuration.config import get_configuration
from utils import auth


@fixture(scope='session')
def config():
    return get_configuration()


@fixture(scope='session')
def logged_in_driver_homepage(base_driver, config):
    auth.login(base_driver, config)

    yield base_driver
    
    auth.logout(base_driver, config)


@fixture(scope="function")
def logged_in_with_item_in_cart(logged_in_driver_homepage, config):
    backpack_add_to_cart_button = logged_in_driver_homepage.find_element(By.ID, config["backpack_add_to_cart_button"])  #noqa: E501
    backpack_add_to_cart_button.click()

    yield logged_in_driver_homepage

    remove_from_cart_button = logged_in_driver_homepage.find_element(By.ID, config["remove_button"])  #noqa: E501
    remove_from_cart_button.click()


@fixture(scope="function")
def logged_in_menu_open(logged_in_driver_homepage, config):
    wait = WebDriverWait(logged_in_driver_homepage, 10)
    burger_icon = wait.until(
        EC.element_to_be_clickable((By.ID, config["burger_icon"]))
    )
    burger_icon.click()

    yield logged_in_driver_homepage

    wait = WebDriverWait(logged_in_driver_homepage, 10)
    burger_icon = wait.until(
        EC.element_to_be_clickable((By.ID, config["burger_close"]))
    )
    burger_icon.click()
