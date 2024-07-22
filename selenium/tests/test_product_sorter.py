from pytest import mark
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@mark.parametrize("drop_down_value", ['hilo', 'za',])
@mark.smoke
@mark.browser
def test_sorter_z_to_a(
    logged_in_driver_homepage,
    drop_down_value,
    config,
):  
    wait = WebDriverWait(logged_in_driver_homepage, 10)
    sorter_drop_down_button = Select(wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, config["sorter_drop_down"]))
    ))

    sorter_drop_down_button.select_by_value(drop_down_value)

    t_shirt_red  = wait.until(
        EC.element_to_be_clickable((By.XPATH, config["t_shirt_red"]))
    )
    assert t_shirt_red.is_displayed()
