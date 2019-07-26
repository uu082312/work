# --coding: utf-8 --
import time


def wrapper(fun):
    def inner(driver, name, index, *args):
        try:
            time.sleep(0.3)
            fun(driver, name, index, *args)
        except:
            time.sleep(1)
            try:
                fun(driver, name,  index, *args)
            except:
                time.sleep(1.5)
                try:
                    fun(driver, name, index, *args)
                except:
                    time.sleep(2.5)
                    try:
                        fun(driver, name, index, *args)
                    except:
                        time.sleep(4)
                        fun(driver, name, index, *args)

    return inner


def wrapper_open_page(fun):
    def inner(driver, *args):
        try:
            time.sleep(0.3)
            fun(driver, *args)
        except:
            time.sleep(1)
            try:
                fun(driver, *args)
            except:
                time.sleep(1.5)
                try:
                    driver.refresh()
                    fun(driver, *args)
                except:
                    time.sleep(2.5)
                    try:
                        fun(driver, *args)
                    except:
                        time.sleep(4)
                        fun(driver, *args)

    return inner


def wrapper_input(fun):
    def inner(driver, khmc, qyzt, i, khid):
        try:
            time.sleep(0.7)
            fun(driver, khmc, qyzt, i, khid)
        except:
            print('----------1--------------')
            time.sleep(0.5)
            try:
                fun(driver, khmc, qyzt, i, khid)
            except:
                print('----------2--------------')

                time.sleep(1)
                try:
                    fun(driver, khmc, qyzt, i, khid)
                except:
                    print('----------3--------------')

                    time.sleep(5)
                    fun(driver, khmc, qyzt, i, khid)

    return inner


def wrapper_city(fun):
    def inner(driver, info_list, *args):
        try:
            time.sleep(0.3)
            fun(driver, info_list, *args)
        except:
            time.sleep(1)
            try:
                fun(driver, info_list, *args)
            except:
                time.sleep(1.5)
                try:
                    fun(driver, info_list, *args)
                except:
                    time.sleep(2.5)
                    try:
                        fun(driver, info_list, *args)
                    except:
                        time.sleep(4)
                        fun(driver, info_list, *args)

    return inner