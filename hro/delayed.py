import time


def wrapper(func):
    def inner(driver, name, *args):
        time.sleep(0.5)
        try:
            func(driver, name, *args)
        except:
            time.sleep(1)
            try:
                func(driver, name, *args)
            except:
                time.sleep(3)
                try:
                    func(driver, name, *args)
                except:
                    time.sleep(5)
                    try:
                        func(driver, name, *args)
                    except:
                        time.sleep(7)
                        func(driver, name, *args)

    return inner
