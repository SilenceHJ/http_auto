
import configparser
import unittest
import pandas as pd

def data(actual,expect):
    print("333")
    assert True

def is_exe_test(str):
    print("222")
    if int(str)==0:
        return "不执行"
    else:
        return ""


if __name__ == '__main__':
    # print("222")
    # config = configparser.ConfigParser()
    # config.read('config/db.ini',encoding='utf-8-sig')
    # print(config.get('dbinfo','username'))
    # print(config.get('dbinfo', 'password'))
    # config.add_section('write')
    # config.set('write','cookies','silence')
    # config.write(open('config/db.ini','a'))


    df = pd.read_excel('testdata/dataexcel.xlsx')
    print(df)
    df = df.query('isexe!=0')
    print(df)
    print(df.to_dict(orient='record'))