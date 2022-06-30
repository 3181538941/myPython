# requests 请求 需要提前在Terminal中安装 pip install requests
import os
import time

import requests
# re正则
import re
# 改变自己身份
headers = {
   'User-Agent': 'asbasdf'
}
# 请求网页
print("请输入你要爬取网站的链接")
httpurl = input()
response = requests.get(httpurl,headers = headers)
print(response.request.headers)
print(response.text)
html = response.text
# 解析网页
# view-source:https://www.vmgirls.com/15159.html
# 链接前加view-source查看网页源代码
dir_name = re.findall('<h1 class="post-title h1">(.*?)</h1>',html)[-1]
if not os.path.exists(dir_name):
   os.mkdir(dir_name)
# 正则查找
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)
print(urls)
# 保存图片
for url in urls:
   time.sleep(1)
   # 图片名字
   name = url.split('/')[-1]
   response = requests.get("https:"+url,headers = headers)
   print(name+"正在下载")
   with open(dir_name+'/'+name,'wb') as f:
       f.write(response.content)
print('下载完毕')