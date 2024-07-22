from pytest import fixture
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

from custom_logger import logger
from configuration.config import get_configuration


@fixture(scope="session")
def base_driver(config):
    logger.info(f"{config['driver_name']} driver")

    seleniumwire_options = {'verify_ssl': False}
    driver_class = webdriver.Chrome
    options = Options()

    if config['driver_headless']:
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-renderer-backgrounding")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-backgrounding-occluded-windows")
        options.add_argument("--disable-client-side-phishing-detection")
        options.add_argument("--disable-crash-reporter")
        options.add_argument("--disable-oopr-debug-crash-dump")
        options.add_argument("--no-crash-upload")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-low-res-tiling")
        options.add_argument("--log-level=3")
        options.add_argument("--silent")

    driver = driver_class(
        options=options,
        seleniumwire_options=seleniumwire_options
    )

    driver.set_window_size(config['driver_width'], config['driver_height'])
    driver.maximize_window()

    driver.get(config['base_url'])
    
    yield driver

    driver.quit()
