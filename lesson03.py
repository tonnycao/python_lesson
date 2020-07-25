"""匿名函数转换"""
print(list(filter(lambda x: x % 2 == 1, range(1, 20))))




"""- 定义一个模块实现网址完整性的校验"""
import re
url = "https://www.programiz.com/python-programming/file-operation"
if re.search("(http|https|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]", url):
    print("It is a valid URL")
else:
    print("It is not a value URL")




"""读取log文件，取出url并输出前10访问量的url"""
file_path = r"C:\Learning\python_lesson\access.log"
with open(file_path, mode="r+", encoding='utf-8') as f:
    file_content = f.read()
    urls = re.findall("http://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]", file_content)
    dic = {}
    for url in urls:
        dic[url] = dic.get(url, 0) + 1
    t = zip(dic.values(), dic.keys())
    order = sorted(t, reverse=True)
    for i in range(0, 10):
        print(order[i])




"""使用os模块实现 shell ls命令"""
import os


def ls(directory_path):
    names = os.listdir(directory_path)
    for name in names:
        print(name)
        if "." not in name:
            sub_directory_path = directory_path + "\\" + name
            ls(sub_directory_path)


directory_path = r"C:\Platform\test_dev02-master"
ls(directory_path)





"""
math
datetime
collections
base64
hashlib
hmac
itertools
XML
HTMLParser
urllib

- 序列化

  ```
  obj = dict(name='曹建', age=30)
  ```

"""


