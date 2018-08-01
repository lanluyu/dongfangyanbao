东方财富网个股研报信息爬虫说明文档
==
介绍
 - 
东方财富网爬虫是一个基于Scrapy-Selenium框架爬取东方财富网的个股研报标题、个股信息以及收益的爬虫。<br>

代码说明
--
### 运行环境
* Windows 10 专业版<br>
* Python 3.5/Scrapy 1.5.0/MongoDB 3.4.7<br>

### 依赖包
* Requests<br>
* Pymongo<br>
* Selenium 3.11.0
* Faker(随机切换User-Agent)<br>

爬取结果
-
在东方财富网上总共爬取了16791条个股研报信息。结果由爬虫先存储在MongoDB中，再导出为Excle文件。部分数据如下截图:<br>
![研报详情截图](https://github.com/lanluyu/dongfangyanbao/blob/master/%E9%83%A8%E5%88%86%E7%A0%94%E6%8A%A5%E4%BF%A1%E6%81%AF.PNG)
