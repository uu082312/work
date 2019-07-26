from hro.loggin import loggin
from hro.read_data import data


if __name__ == '__main__':
    data_list = data()
    loggin(data_list)
