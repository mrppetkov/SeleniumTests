from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login(driver, config):
    username_field = driver.find_element(By.ID, config["username_field"])
    username_field.send_keys(config['input_registered_email'])

    password_field = driver.find_element(By.ID, config["password_field"])
    password_field.send_keys(config['input_registered_password'])

    login_button = driver.find_element(By.ID, config["login_button"])
    login_button.click()


def logout(driver, config):
    wait = WebDriverWait(driver, 10)
    burger_icon = wait.until(
        EC.element_to_be_clickable((By.ID, config["burger_icon"]))
    )
    burger_icon.click()
    
    logout_button = wait.until(
        EC.element_to_be_clickable((By.ID, config["burger_menu_logout_button"]))  # noqa: E501
    )
    logout_button.click()
