#!/user/bin/env python
# -*- conding:utf-8 -*-
from time import sleep

import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    # 引入Chromedriver
    driver = webdriver.Chrome("../chrome_driver_v78/chromedriver.exe")

    sleep(1)
    driver.maximize_window()
    sleep(1)
    yield driver
    driver.quit()