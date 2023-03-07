import requests
import random
import string
import time
from bs4 import BeautifulSoup
import pandas
import numpy
import pandas as pd
from pandas import Series

# 生成随机用户名
def user(t):
    # 第一种方法
    usr = []
    for j in range(t):
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(8):
            sa.append(random.choice(seed))
        salt = ''.join(sa)
        usr.append(salt)
    return usr

# 生成随机邮箱
def e_mail(m):
    fond = []
    for x in range(m):
        fond.append('@qq.com')
    intmail = [random.randint(100000, 9999999999) for i in range(m)] # 生成随机QQ号
    mail = []
    for k in intmail:
        mail.append(str(k))
    result = [c + e for c, e in zip(mail, fond)]
    return result

# 生成随机密码
def pwda(n):
    pwds = [random.randint(10000000, 99999999) for i in range(n)] # 8位数密码
    return pwds

cont = int(input('请输入创建次数:>'))
user = user(cont)
emails = e_mail(cont)
password = pwda(cont)
df = pd.DataFrame({'user': user,
                'e-mail': emails,
                'password': password})

df.to_csv('user.csv',index=False)
data = pd.read_csv('user.csv')
with open('user.txt','a+') as f:    # 新建一个txt空文档
    for line in data.values:
        f.write((str(line[0])+'\t'+str(line[1])+'\t'+str(line[2])+'\n'))
