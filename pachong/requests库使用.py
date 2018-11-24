#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: dj
@contact: dj@itmojun.com
@software: PyCharm
@file: main.py
@time: 2018/10/30 14:09
"""

import requests
from lxml import etree

def main():

    # r = requests.get("http://war.163.com/")
    #
    # root = etree.HTML(r.text)
    #
    # for element in root.xpath("/html/body/div[1]/div[3]/div[3]/div[2]/ul//a"):
    #     print(element.text)

    # while True:
    #     r = requests.post("http://pangshe.com/guestbook.php", {"sayer":"魔君".encode("gb2312"), "msg":"你好，中国".encode("gb2312"), "submitbtn":"发布留言".encode("gb2312")})
    #     print(r.status_code)
    #     # r.encoding = "gb2312"
    #     # print(r.text)

    r"""
    /html/body/div[1]/div[3]/div[3]/div[2]/ul/li[1]/a
    /html/body/div[1]/div[3]/div[3]/div[2]/ul/li[2]/a
    """

    person_id = input("请输入身份证号：")
    url_params = {"key":"73e721987069bcc52efa969fb4a64830", "cardno":person_id}
    r = requests.get("http://apis.juhe.cn/idcard/index", url_params)
    r = r.json()
    # print(r)
    if r["error_code"] == 0:
        print("区域：%s\n性别：%s\n生日：%s" % (r["result"]["area"], r["result"]["sex"], r["result"]["birthday"]))
    else:
        print(r["reason"])

if __name__ == '__main__':
    main()
