# coding: utf-8
import time
import win32gui
import win32con
from selenium import webdriver
from hro.get_element import get_elememt_by_id_send, get_elememt_by_id_click
from hro.get_element import get_elememts_by_class_click
from hro.get_element import get_element_by_css_doubclick
from hro.get_element import get_element_by_xpath_send
from hro.read_data import data


def loggin(data_list):
    url = "http://hro.joyohro.com/login.html"
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    driver = webdriver.Chrome(chrome_options=option)
    driver.implicitly_wait(4)
    driver.get(url)
    get_elememt_by_id_send(driver, "loginCode", 13588204770)
    get_elememt_by_id_send(driver, "password", "Fubin2613")
    try:
        el = driver.find_element_by_id("captchaCode")
        yzm = input("请输入验证码: ")
        el.send_keys(yzm)
        get_elememt_by_id_click(driver, "loginbtn")
    except:
        pass
    get_elememt_by_id_click(driver, "tg_switch_roletype")
    time.sleep(1)
    chose_shebao = driver.find_element_by_id("tg_switch_roletype")
    shebao = chose_shebao.find_element_by_xpath("./option[2]")
    shebao.click()
    time.sleep(5)
    # 社保政策
    get_elememt_by_id_click(driver, "node0")
    get_elememts_by_class_click(driver, "childchg", 2)
    add_input(driver, data_list)
    # import_input(driver)


def add_input(driver, data_list):

    # 读取信息
    # data_list = data()
    for index, one_info in enumerate(data_list):
        # 新增
        get_elememt_by_id_click(driver, "bn_add_jq_ssec_propchange")
        # 拉开社保政策
        get_elememt_by_id_click(driver, "procPlic_sel")
        # 查询
        # content = "苏州[园区乙类]社保政策（北京外企德科）"
        get_elememt_by_id_send(driver, "com_sel_search_obj", one_info[0])
        get_elememt_by_id_click(driver, "com_sel_qksearch")
        # 选择政策
        name = "td[title='%s']" % one_info[0]
        get_element_by_css_doubclick(driver, name)
        # 点开社保
        get_elememt_by_id_click(driver, "procIns_sel")
        get_element_by_css_doubclick(driver, "td[title=%s]" % one_info[1])

        # if not one_info:
        #     continue
        # get_elememts_by_class_send(driver, "add_input", index, one_info[0])
        # 输入信息
        ele_idaaa = ["procNewhbase", "procNewhbasep", "procNewlbase", "procNewlbasep", "procNewcprop", "procNewpprop",
                     "procNewcproppay", "procNewpproppay", "procNewcamon", "procNewpamon"]
        for info_index, el_id in enumerate(ele_idaaa, 2):
            info = one_info[info_index]
            # 如果没有内容跳过
            if not info:
                continue
            info = "{:g}".format(one_info[info_index])
            get_elememt_by_id_send(driver, el_id, info)
        get_elememt_by_id_click(driver, "procNewcrule")
        # 调整后企缴小数位规则
        qgz = driver.find_elements_by_xpath("//select[@id='procNewcrule']/option")
        for ele in qgz:
            if ele.text == one_info[12]:
                ele.click()
                time.sleep(0.1)
                ele.click()
                break
        get_elememt_by_id_click(driver, "procNewprule")
        qgz = driver.find_elements_by_xpath("//select[@id='procNewprule']/option")
        for ele in qgz:
            if ele.text == one_info[13]:
                ele.click()
                time.sleep(0.1)
                ele.click()
                ele.click()
                break
        # 收费月 打开日期
        get_elememt_by_id_click(driver, "procPaymonth_sel")
        # 查询
        get_elememt_by_id_send(driver, "com_sel_search_obj", int(one_info[14]))
        get_elememt_by_id_click(driver, "bn_searchtb_com_sel_obj")
        get_element_by_css_doubclick(driver, "td[title='%s']" % int(one_info[14]))
        # 生效日期
        get_elememt_by_id_click(driver, "procPerid_sel")
        get_element_by_xpath_send(driver, "//div[@class='ui-grid-qkshdiv']/input", int(one_info[15]))
        # 查询
        get_elememt_by_id_click(driver, "bn_searchtb_com_sel_obj")
        get_element_by_css_doubclick(driver, "td[title='%s']" % int(one_info[15]))
        time.sleep(10)


def import_input(driver):
    get_elememt_by_id_click(driver, "bn_imp_jq_ssec_propchange")
    get_elememt_by_id_click(driver, "impFile")
    time.sleep(5)
    dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, r'C:\Users\andap\Desktop\imptmp_propchange.xls')  # 往输入框输入绝对地址
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    time.sleep(10)


if __name__ == '__main__':
    data_list = data()
    loggin(data_list)
    time.sleep(10000)
