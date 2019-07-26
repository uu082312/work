from hro.delayed import wrapper
from selenium.webdriver.common.action_chains import ActionChains



@wrapper
def get_elememt_by_id_send(driver, name, content):
    el = driver.find_element_by_id(name)
    el.clear()
    el.send_keys(str(content))


@wrapper
def get_elememt_by_id_click(driver, name):
    el = driver.find_element_by_id(name)
    el.click()


@wrapper
def get_elememts_by_class_click(driver, name, index):
    el = driver.find_elements_by_class_name(name)[index]
    el.click()


@wrapper
def get_elememts_by_class_send(driver, name, index, content):
    el = driver.find_elements_by_class_name(name)[index]
    el.clear()
    el.send_keys(str(content))


@wrapper
def get_element_by_css_doubclick(driver, name):
    el = driver.find_element_by_css_selector(name)
    ActionChains(driver).double_click(el).perform()


@wrapper
def get_element_by_css_send(driver, name, content):
    el = driver.find_element_by_css_selector(name)
    el.clear()
    el.send_keys(str(content))


@wrapper
def get_elememt_by_id_doubclick(driver, name):
    el = driver.find_element_by_id(name)
    ActionChains(driver).double_click(el).perform()


@wrapper
def get_element_by_xpath_send(driver, name, content):
    el = driver.find_element_by_xpath(name)
    el.clear()
    el.send_keys(str(content))
