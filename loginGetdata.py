#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

import requests, Cookie, base64, urllib3, time, random
from bs4 import BeautifulSoup
from ua import get_ua
from colorama import init
init(autoreset=True)

class myFofaSpider():
    def __init__(self, pstar=1):
        self.cookie = Cookie.Cookie
        self.pstar = pstar

    def getData(self, query, page, pgSize=10):
        query = str(base64.b64encode(query.encode()))[2:-1].format(query)
        for p in range(1, page+1):
            #all_url = f"https://fofa.info/result?qbase64={query}&full=true&page={p}&page_size={pgSize}"
            url = f"https://fofa.info/result?qbase64={query}&page={p}&page_size={pgSize}"
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            headers = {
                "User-Agent": get_ua.random_ua(self),
                "Cookie": self.cookie
            }
            try:
                respon = requests.get(url=url, headers=headers, timeout=6).text
                soup_data1 = BeautifulSoup(respon, "html.parser")
                match_result = soup_data1.find_all("span", class_="pSpanColor")[0].contents[0]
                print("")
                print("\033[36m[+] 一共查询到"+ match_result +"条结果")
                print("正在获取第" + str(p) + "页URL(IP)...")

                #提取需要的标签
                urlsList = soup_data1.find_all("span", class_="aSpan")
                # for循环匹配获取URL
                for i in range(len(urlsList)):
                    match_urls_data = str(urlsList[i].contents)
                    match_urls = match_urls_data.split('"')[1]
                    print("\033[31m[+] " + match_urls)
                    with open("res_urls.txt", "a+") as fw:
                        fw.writelines(match_urls + "\n")
            except Exception:
                print("请求失败！可能Cookie过期，请再次尝试！")
                print("\033[31m[+] 温馨提示：如果您不是会员，page数不能大于5。")
                break
                page = self.pstar + 1
                t = random.randint(2, 5)
                time.sleep(t)
