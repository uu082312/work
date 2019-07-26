import time
from hro.tw.get_element import get_element_by_class_name_send, get_element_by_class_name_click


def func(driver, info_element, lie, content, start=None, end=None):
    jnbl_list = info_element.find_elements_by_xpath("./tbody/tr/td[%d]" % lie)[start: end]
    for index, jsxx in enumerate(jnbl_list):
        ret = content[index]
        if not ret:
            continue
        jsxx.click()
        ret = "{:g}".format(ret)
        # print(ret)
        get_element_by_class_name_send(driver, "input-sm", str(ret))
        get_element_by_class_name_click(driver, "editable-submit", "")
        time.sleep(0.3)