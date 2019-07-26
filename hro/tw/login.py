# coding: utf-8
import time
from selenium import webdriver
from hro.tw.get_element import get_elements_by_class_name_click, get_elements_by_class_name_send
from hro.tw.get_element import get_element_by_css_selector_click
from hro.tw.get_element import get_element_by_class_name_send, get_element_by_class_name_click
from hro.tw.input_info import func
from hro.tw.read_data import data
from hro.tw.delayed import wrapper_open_page, wrapper, wrapper_city


def main_fnc(url, user, password):
    driver = login(url, user, password)
    open_page(driver)


def login(url, user, password):
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    driver = webdriver.Chrome(chrome_options=option)
    driver.implicitly_wait(4)
    driver.get(url)
    driver.maximize_window()
    # time.sleep(5)
    username = driver.find_element_by_id("username")
    username.clear()
    username.send_keys(user)
    pwd = driver.find_element_by_id("password")
    pwd.clear()
    pwd.send_keys(password)
    time.sleep(1)
    submit = driver.find_element_by_id("submit_button")
    submit.click()
    # open_page(driver)
    return driver


@wrapper_open_page
def open_page(driver):
    get_elements_by_class_name_click(driver, "waves-button", 6)
    menu = driver.find_elements_by_class_name("sub-menu")[0]
    lr = menu.find_element_by_xpath("./li[1]")
    lr.click()
    # time.sleep(1)
    chose_city_info(driver)


@wrapper_open_page
def chose_city_info(driver):
    click_city = driver.find_element_by_class_name("js-city")
    click_city.click()
    # time.sleep(1)
    ret = data()
    sf = ret[1]
    # 选择省份
    get_element_by_css_selector_click(driver, "a[title=%s]", sf)
    city = ret[2]
    get_element_by_css_selector_click(driver, "a[title=%s]", city)
    content = ret[3]
    get_elements_by_class_name_send(driver, "typeahead-address", 1, content)
    # 选择时间
    get_elements_by_class_name_click(driver, "typeahead-effectiveTime", 0)
    get_elements_by_class_name_click(driver, "typeahead-effectiveTime", 1)
    chose_time = ret[4]
    if chose_time == "前":
        tt = driver.find_elements_by_class_name("tt-menu")[1]
        tt.find_elements_by_class_name("tt-selectable")[0].click()
    else:
        tt = driver.find_elements_by_class_name("tt-menu")[1]
        tt.find_elements_by_class_name("tt-selectable")[-1].click()
    # 进入
    get_element_by_class_name_click(driver, "btn-search", "")
    info_list = ret[0]
    click_ctiy(driver, info_list, ret)


@wrapper_city
def click_ctiy(driver, info_list, ret):
    el = driver.find_element_by_class_name("tap-wrap")
    e = el.find_elements_by_xpath('./ul/li/span')
    # 修改
    get_elements_by_class_name_click(driver, "update-five", 0)
    flag = True
    n = 0
    for chose, i in enumerate(e):

        i.click()
        # 公积金的修改
        if flag:
            flag = False
            get_elements_by_class_name_click(driver, "update-fund", 0)

        index = chose + n
        func_gjj(driver, ret, index)
        # 写数据
        js3 = "window.scrollTo(0,1500)"
        driver.execute_script(js3)
        write_info(driver, info_list, chose)
        n += 1


@wrapper
def write_info(driver, info_list, chose):
    info_element = driver.find_elements_by_class_name("five-table")[chose]
    for index, info_content in enumerate(info_list, 2):
        if index > 7:
            index += 3
        if index in (4, 5, 7, 12, 14):
            start = 0
            end = 3
        else:
            start = None
            end = None
        try:
            func(driver, info_element, index, info_content, start, end)
        except:
            time.sleep(2)
            func(driver, info_element, index, info_content, start, end)


def func_gjj(driver, ret, chose):

    time.sleep(1)
    # 1--1  2--3 3--5 4--7
    element_obj = driver.find_elements_by_class_name("wbg")[chose]
    el_list = element_obj.find_elements_by_xpath("./th/span")
    gjj = ret[0]
    for i, el in enumerate(el_list):
        gjj_ret = gjj[i][-1]
        if not gjj_ret:
            continue
        el.click()
        # print(type(gjj_ret),'gjj_ret')
        # gjj_ret = "{:g}".format(gjj_ret)
        get_element_by_class_name_send(driver, "input-sm", str(gjj_ret))
        get_element_by_class_name_click(driver, "editable-submit", "")


if __name__ == '__main__':
    login("https://tianwu.joyowo.com/admin/", "luoxy", "Fubin@2613")
    time.sleep(10000)
