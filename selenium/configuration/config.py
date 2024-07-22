import os

from pydantic_settings import BaseSettings


ENV_PATH = ".env"


class Selectors(BaseSettings):
    #Login
    username_field: str = 'user-name'
    password_field: str = 'password'
    login_button: str = 'login-button'
    #Home page
    shopping_cart_badge: str = 'shopping_cart_badge'
    burger_icon: str = 'react-burger-menu-btn'
    burger_close: str = "react-burger-cross-btn"
    burger_menu_logout_button: str = 'logout_sidebar_link'
    burger_menu_about_button: str = 'about_sidebar_link'
    backpack_add_to_cart_button: str = 'add-to-cart-sauce-labs-backpack'
    remove_button: str = 'remove-sauce-labs-backpack'
    cart_icon: str = 'shopping_cart_container'
    sorter_drop_down: str = '.product_sort_container'
    sorter_option_z_to_a: str = '//*[@id="header_container"]/div[2]/div/span/span'
    t_shirt_red: str = '//*[@id="item_3_title_link"]'
    #Cart
    continue_shoppimg_button: str = 'continue-shopping'
    remove_button_cart: str = '#remove-sauce-labs-backpack'
    #About page
    about_page_try_it_free: str = '__next'

class Config(BaseSettings):
    base_url: str
    about_us_path: str = "company/about-us"
    driver_name: str = "Chrome"
    wait_timeout: int = 10
    max_response_time: int = 5000
    max_total_size: int = 10485760
    driver_headless: bool = False
    driver_width: int = 1920
    driver_height: int = 1080
    #
    input_registered_password: str = ""
    input_registered_email: str = ""


class Configuration(Config, Selectors):

    class Config:
        case_sensitive: bool = False
        env_file = ENV_PATH
        env_prefix = "CFG_"


def get_config_env(config):
    for key, value in os.environ.items():
        if key.startswith("CFG_"):
            config[key[4:].lower()] = value

    return config


def get_configuration() -> dict[str, str]:
    config = Configuration().model_dump()
    config = get_config_env(config)
    # print(f"config: {config}")
    return config
