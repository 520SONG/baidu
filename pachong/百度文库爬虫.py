#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: dj
@contact: dj@itmojun.com
@software: PyCharm
@file: main.py
@time: 2018/10/31 10:37
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from lxml import etree
import re

def main():
    browser = webdriver.Chrome()
    browser.get('https://wenku.baidu.com/view/fbdc423a3968011ca30091f0.html')
    browser.set_window_size(1024, 6000)
    elem = browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[6]/div[2]/div[1]/span")
    # elem.click()
    f = open("pid_data.txt", "w", encoding="utf-8")
    for i in range(2, 83):
            print(i)
            elem = browser.find_elements_by_css_selector("input.page-input")
            elem[0].clear()
            elem[0].send_keys(str(i), Keys.RETURN)
            time.sleep(10)
            page = str(browser.page_source)
            root = etree.HTML(page)
            p_list = root.xpath("//div[@id='pageNo-%d']//p" % i)
            cnt = 1
            for p in p_list:
                if len(p.text) == 1 or len(p.text) == 2:
                    continue
                if "，" in p.text:
                    continue
                if re.match("\d{6}", p.text):
                    p.text = p.text[0:6]
                if re.fullmatch("\d{6}", p.text) == None and "省" not in p.text and "市" not in p.text and "区" not in p.text and "县" not in p.text:
                    continue
                print(p.text)
                if cnt % 2 != 0:
                    f.write(p.text)
                else:
                    f.write(" " + p.text + "\n")
                cnt += 1
                f.flush()
    f.close()
    # with open("test.html", "w", encoding="utf-8") as f:
    #     f.write(page)

    # page = browser.find_elements_by_css_selector("#pageNo-2")
if __name__ == '__main__':
    main()
