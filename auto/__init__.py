# # coding:utf-8

import requests
import random
import string
import time
import pandas
import numpy
import pandas as pd
from pandas import Series
from selenium import webdriver
from selenium.webdriver.common.by import By
import readuser

# 读取用户名文件，并输出
def csv_file_read():
    csv_result = pd.read_csv('user.csv')
    row_list = csv_result.values.tolist()
    return row_list

datafrom = csv_file_read()
user = []
eemail = []
password = []
cont = int(input('生成账户次数:>'))
for n in range(cont):
    for i in datafrom:
        user = datafrom[n][0]
        eemail = datafrom[n][1]
        password = datafrom[n][2]

    print(user,eemail,password)
    data = {
        'name': user,
        'email': eemail,
        'passwd': password,
        'repasswd': password
    }

    repose = requests.post('https://shynia.com/auth/register',data=data)
    time.sleep(2.5)
    if(repose.text != ''):
    # print(repose.text)
        print("注册成功!")
        print("正在自动登录...")
    else:
        time.sleep(2.5)
    # ChromeOptions() 函数中有谷歌浏览器的一些配置
    options = webdriver.ChromeOptions()
    # 告诉谷歌这里用的是无头模式
    options.add_argument('headless')
    # 创建谷歌浏览器对象
    driver = webdriver.Chrome('/Users/shenyu/Documents/chromedriver') # 谷歌驱动存放路径
    url = 'https://shynia.com/auth/login'
    driver.get(url)

    driver.find_element(By.ID, 'email').send_keys(eemail)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login_submit').click()
    time.sleep(30)

driver.quit()
