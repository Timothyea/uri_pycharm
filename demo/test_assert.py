#!/user/bin/env python
# -*- conding:utf-8 -*-
from time import sleep

# 展示文本断言
def test_text(driver):
    driver.get("http://ui.yansl.com/#/message")
    # 获取元素，列表形式
    buttons = driver.find_elements_by_xpath("(//label[contains(text(),'自动关闭提示')]/..//span)[2]")
    buttons[0].click()
    message = driver.find_element_by_xpath("//div[@role='alert']/p")
    # 取展示文本
    text = message.text
    print(text)
    # 断言文本条件
    assert "恭喜你，这是一条成功消息" in text
    sleep(2)

# 界面源代码断言
def test_page_scource(driver):
    driver.get("http://ui.yansl.com/")
    driver.find_element_by_xpath("(//div[@style='padding-left: 20px;'])[3]").click()
    sleep(2)
    driver.find_element_by_xpath("//li[contains(text(),'消息提示')]").click()
    sleep(2)
    # 获取整个页面的源代码
    source = driver.page_source
    print(source)
    assert "手工关闭提示" in source
    sleep(2)
