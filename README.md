# domain_addr
 		快速查询当前domain对应IP的地理位置

​		在我的工作中，经常会浏览国外的网站，因为vpn的原因，某些无法访问的网站需要排查原因，到底它是哪个国家的。每次都需要打开cmd终端`ping example.com`，得到ip地址后进行百度查询。如果频繁查询的话，确实感觉浪费时间。

#### 当前项目的执行逻辑：

​		先检查本地网络是否可以联网，获取剪切板最后一条内容，向ip138查询ip的地理位置。

#### 如何使用：

​		依赖包：`re,requests,win32con,win32clipboard,os`

​		首先需要复制一段网址内容：`http://example.com`or `https://example.com`

​		然后cmd终端执行：`python test.py` 即可

#### 结语：

​		代码写得草率，欢迎交流。

​		ip138的查询频率：每个主机IP每日查询1000次。