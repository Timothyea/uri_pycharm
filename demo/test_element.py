#!/user/bin/env python
# -*- conding:utf-8 -*-
from time import sleep

# 纯文本输入
import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_input(driver):
    # 打开网址
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)
    # 元素定位
    input = driver.find_element_by_xpath("//input[@name='t1']")
    input.clear()# 清空
    input.send_keys("窗前明月光")# 发送消息
    sleep(2)

# 单选框
def test_input(driver):
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)

    radio = driver.find_element_by_xpath("//input[@name='sex'][2]")
    # 点击
    radio.click()
    sleep(2)

# 多选框
def test_input_a(driver):
    driver.get("http://ui.yansl.com/#/checkbox")
    sleep(2)

    checkbox = driver.find_element_by_xpath("//span[@class='el-checkbox__inner']")
    # 获得属性
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
    # 模拟鼠标或键盘
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
    # 模拟移动，抓住，按xxx移动，释放，运行以上操作
    actions.drag_and_drop_by_offset(slider,0,-200).perform()
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
    # 以下是固定的代码
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
    # 弹出弹框
    alert = driver.switch_to.alert
    alert.accept()
    sleep(2)

# 窗口切换
def test_alter2(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)

    # 点击超链接
    dang_dang = driver.find_element_by_link_text("当当")
    action = ActionChains(driver)
    # 动作：放下鼠标，点击，抬起鼠标，表演（运行）
    action.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    sleep(2)
    jd = driver.find_element_by_link_text("京东")
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    sleep(2)
    dn = driver.find_element_by_partial_link_text("度娘")
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(dn).key_up(Keys.CONTROL).perform()
    sleep(2)

    # 获取所有窗口的句柄
    handles = driver.window_handles
    for h in handles:
        # 根据窗口句柄，切换窗口
        driver.switch_to_window(h)
        sleep(2)
    # 停在想停的窗口
        if driver.title.__contains__("京东"):
            break



