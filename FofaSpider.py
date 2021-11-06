#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

from loginGetdata import myFofaSpider
import argparse

def title():
    print("")
    print('*'.center(60, '*'))
    print("github：https://github.com/ltfafei".center(50))
    print("CSDN: afei00123.blog.csdn.net".center(50))
    print("公众号：网络运维渗透".center(35))
    print("")
    print('*'.center(60, '*'))
    print("")

if(__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="FofaSpider")
    parser.add_argument(
        '-q', '--query', type=str, required=True,
        help="Please input query target. eg: title='管理后台'"
    )
    parser.add_argument(
        '-p', '--page', type=int, default=1,
        help='Please input start query page. eg: 5'
    )
    args = parser.parse_args()
    run = myFofaSpider()
    try:
        if args.query and args.page:
            run.getData(args.query, args.page)
            print("")
            print('*'.center(40, '*'))
            print("\033[33m[+] URL保存在res_urls.txt中。")
    except Exception:
        print("请使用-h选项查看帮助信息。")