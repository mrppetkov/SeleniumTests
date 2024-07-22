from pytest import mark
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import auth


@mark.smoke
@mark.browser
def test_auth_flow(
    base_driver,
    config,
):
    auth.login(base_driver, config)
    wait = WebDriverWait(base_driver, 10)
    burger_icon = wait.until(
        EC.element_to_be_clickable((By.ID, config["burger_icon"]))
    )
    assert burger_icon.is_displayed()

    auth.logout(base_driver, config)

    username_field = wait.until(
        EC.element_to_be_clickable((By.ID, config["username_field"]))
    )
    assert username_field.is_displayed()
