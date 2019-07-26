# coding: utf-8
import xlrd


def data():
    ret = xlrd.open_workbook('C:\\Users\\andap\Desktop\\test.xls')
    table = ret.sheet_by_name('Sheet1')
    s = table.cell(1, 11).value
    c = table.cell(1, 12).value
    j = table.cell(1, 13).value
    t = table.cell(1, 14).value

    # print('s', s, type(s), c, j)
    # 获取行
    h = table.nrows
    # 获取列
    l = table.ncols
    info = []

    for lie in range(1, l-3):
        one_info = []
        for hang in range(1, h):
            v = table.cell(hang, lie).value
            one_info.append(v)
        info.append(one_info)

    return info, s, c, j, t


if __name__ == '__main__':
    print(data())