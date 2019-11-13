#!/user/bin/env python
# -*- conding:utf-8 -*-
from time import sleep

# 纯文本输入
import autoit
from selenium.webdriver import ActionChains


def test_input(driver):
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)

    input = driver.find_element_by_xpath("//input[@name='t1']")
    input.clear()# 清空
    input.send_keys("窗前明月光")
    sleep(2)

# 单选框
def test_input(driver):
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)

    radio = driver.find_element_by_xpath("//input[@name='sex'][2]")
    radio.click()
    sleep(2)

# 多选框
def test_input_a(driver):
    driver.get("http://ui.yansl.com/#/checkbox")
    sleep(2)

    checkbox = driver.find_element_by_xpath("//span[@class='el-checkbox__inner']")
    attribute = checkbox.get_attribute("class")
    if not attribute =="el-checkbox__input is-checked":
        checkbox.click()
        sleep(2)

# 下拉框
def test_select(driver):
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)

    select = driver.find_element_by_xpath("//input[@style='height: 40px;']")
    select.click()

    sleep(2)
    option = driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    # 模拟鼠标
    actions = ActionChains(driver)
    # 模拟鼠标移动
    actions.move_to_element(option).perform()
    sleep(2)
    option.click()
    sleep(2)

# 滑块
def test_slider(driver):
    driver.get("http://ui.yansl.com/#/slider")
    sleep(2)

    slider = driver.find_element_by_xpath("(//div[@class='el-tooltip el-slider__button'])[last()]")
    sleep(2)
    actions = ActionChains(driver)
    actions.move_to_element(slider).click_and_hold(slider).move_by_offset(0,-200).release(slider).perform()
    sleep(2)

# 时间
def test_time(driver):
    driver.get("http://ui.yansl.com/#/dateTime")
    sleep(2)

    tl = driver.find_element_by_xpath("//input[@class='el-input__inner']")
    tl.clear()# 清空
    tl.send_keys("15:15:00")
    sleep(2)

# 选择文件上传
def test_file(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)

    file = driver.find_element_by_xpath("(//div[1]//input)[1]")
    file.click()# 清空
    file.send_keys("C:\\Users\\guoya\\Desktop\\123.csv")
    sleep(2)

# 点击上传
def test_file2(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)

    file = driver.find_element_by_xpath("(//span[text()='点击上传'])[1]")
    file.click()
    sleep(2)
    autoit.win_wait("打开", 10)
    sleep(1)
    # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "C:\\Users\\guoya\\Desktop\\123.csv")
    sleep(2)
    autoit.control_click("打开", "Button1")
    sleep(2)

# 点击提交,点击确定
def test_alter(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)

    botton = driver.find_element_by_xpath("/html/body/table/tbody/tr[6]/td[2]/input")
    botton.click()
    sleep(2)
    alert = driver.switch_to.alert
    alert.accept()
    sleep(2)

