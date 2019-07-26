# coding: utf-8
import xlrd


def data():
    ret = xlrd.open_workbook('C:\\Users\\andap\Desktop\\hro.xls')
    table = ret.sheet_by_name('Sheet1')
    # 获取行
    h = table.nrows
    # 获取列
    l = table.ncols
    info = []

    for hang in range(1, h):
        one_info = []
        for lie in range(l):
            v = table.cell(hang, lie).value
            one_info.append(v)
        info.append(one_info)

    return info


if __name__ == '__main__':
    print(data())