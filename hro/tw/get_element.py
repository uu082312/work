import time
from hro.tw.delayed import wrapper


@wrapper
def get_elements_by_class_name_click(driver, name, index):
    el = driver.find_elements_by_class_name(name)[index]
    el.click()


@wrapper
def get_elements_by_class_name_send(driver, name, index, content):
    el = driver.find_elements_by_class_name(name)[index]
    el.clear()
    el.send_keys(content)


@wrapper
def get_element_by_css_selector_click(driver, value, content):
    el = driver.find_element_by_css_selector(value % content)
    el.click()


@wrapper
def get_element_by_class_name_send(driver, name, content):
    el = driver.find_element_by_class_name(name)
    el.clear()
    el.send_keys(content)


@wrapper
def get_element_by_class_name_click(driver, name, content):
    el = driver.find_element_by_class_name(name)
    el.click()
