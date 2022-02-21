## 免责声明
使用本工具请遵守《网络安全法》

## 使用说明
### FofaSpider_v1.0使用说明：
    FofaSpider_v1.0的时候，fofa全局采用Cookie进行鉴权。近段时间fofa升级了（听说封闭开发了一周），突然发现FofaSpider不能用了，抓包发现资产查询时不在使用Cookie鉴权，而使用了JWT进行鉴权，所以FofaSpider也该升级了。
```
  FofaSpider基于python3编写，使用请安装python3环境。
  
1、首先将你的Fofa cookie粘贴复制到Cookie.py中（Cookie = "your fofa cookie"）
2、-q 参数指定查询Fofa语法；
3、-p 参数指定爬取页数（非Fofa会员只能爬取前五页，不指定默认爬取第一页）；
4、爬取结果默认追加保存至res_urls.txt。
```

## 依赖安装
`pip install -r requirements.txt`


## 使用演示

`python FofaSpider.py -q title='管理后台'`

![image](https://user-images.githubusercontent.com/43526141/140609676-cfe59554-96be-4101-b322-f9c96258c388.png)


`python FofaSpider.py -q "domain='baidu.com'||title='百度'" -p 5`

![image](https://user-images.githubusercontent.com/43526141/140609708-e3aa0789-c335-4480-bdac-72f46a41ef43.png)

`python FofaSpider.py -q "app=\"泛微-协同办公OA\" && before=\"2022-02-01\" && after=\"2022-01-01\""` -p 1000
![image](https://user-images.githubusercontent.com/43526141/153793194-f08bdbd5-3a63-4db6-8a04-122e3f69f7a3.png)
