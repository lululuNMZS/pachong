# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
import requests
import time
import os


###请求网页###

#反爬 注意User-Agent格式为 'User-Agent': '...'
#user-agent 在浏览器network 找到网页  Headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
}

response = requests.get('https://www.vmgirls.com/12985.html', headers=headers)
#print(response.request.headers)
#print(response.text)
html = response.text

###解析网页###
#正则表达式将（）中的内容保存为list
urls = re.findall('<img alt=".*?" .*? data-pagespeed-lsc-url="(.*?)"', html)

dir_name = re.findall('<img alt="(.*?)" .*? data-pagespeed-lsc-url=".*?"', html)[0]
if not os.path.exists("d:/Download/"+dir_name):
    os.mkdir("d:/Download/"+dir_name)
#print(urls)

###保存图片###
for url in urls:
    time.sleep(1)
    #图片的名字
    img_name = url.split('/')[-1]
    img_response = requests.get(url, headers=headers)
    with open("D:/Download/"+dir_name+'/'+img_name, 'wb') as f:
        f.write(img_response.content)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
