from conftest_base import *
from conftest_selenium import *


def pytest_addoption(parser):
    parser.addoption(
        "--config",
        action="store",
        default="config.json",
        help="Specify the configuration file",
    )
