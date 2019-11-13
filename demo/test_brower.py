#!/user/bin/env python
# -*- conding:utf-8 -*-
from time import sleep




from selenium import webdriver
# 打开游览器
def test_brower(driver):
    driver.get("http://www.baidu.com")
    sleep(1)
    driver.get("http://www.jd.com")
    sleep(1)

    driver.back()
    sleep(1)
    driver.forward()
    sleep(1)
    driver.refresh()
    sleep(1)


# 关闭浏览器，不退出driver
# driver.close()
# 关闭浏览器，退出driver
# driver.quit()