## 免责声明
使用本工具请遵守《网络安全法》

## 使用说明
```
  FofaSpider基于python3编写，使用请安装python3环境。
1、首先将你的Fofa cookie粘贴复制到Cookie.py中（Cookie = "your fofa cookie"）
2、-q 参数指定查询Fofa语法；
3、-p 参数指定爬取页数（非Fofa会员只能爬取前五页，不指定默认爬取第一页）；
4、爬取结果默认追加保存至res_urls.txt。
```

## 依赖安装
`pip install -r requirements.txt`

## 使用
```
`python FofaSpider.py -q title='管理后台'`
`python FofaSpider.py -q "domain='baidu.com'||title='百度'" -p 5`
```
