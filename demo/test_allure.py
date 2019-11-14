#!/user/bin/env python
# -*- conding:utf-8 -*-
from time import sleep

import allure

@allure.feature("一级分类")
@allure.story("二级分类")
@allure.title("标题")
@allure.issue("http://www.baidu.com",'bug')
@allure.testcase("http://www.baidu.com",'用例')
def test_report(driver):
    url = "http://ui.yansl.com/#/checkbox"
    with allure.step("打开网页：{}".format(url)):pass
    driver.get(url)
    with allure.step("点击多选框:{}".format("//input[@value='1']")):
        allure.attach(driver.get_screenshot_as_png(),'',allure.attachment_type.PNG)
    driver.find_element_by_xpath("//input[@value='1']").click()
    with allure.step("点击多选框:{}".format("//input[@value='2']")):
        allure.attach(driver.get_screenshot_as_png(), '', allure.attachment_type.PNG)
    driver.find_element_by_xpath("//input[@value='2']").click()
    sleep(5)








