import urllib.request as ul_request
import urllib.parse as up
import json

to_be_translate = input("请输入您想要翻译的内容: ")
url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
data = {
    'i': to_be_translate,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '16355890253707',
    'sign': '254cb9803ca6a3a83dac0e1bc0484f8c',
    'lts': '1635589025370',
    'bv': "36756d23dc251cc14bf9558b9730e3a5",
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
data = up.urlencode(data).encode('utf-8')
response = ul_request.urlopen(url, data)
html = response.read().decode('utf-8')
print(html)
result = json.loads(html)['translateResult'][0][0]['tgt']
print("翻译的结果是: %s" % result)

