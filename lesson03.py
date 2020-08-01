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
file_path = r"/Users/jimmy/PycharmProjects/python_lesson/access.log"
with open(file_path, mode="r+", encoding='utf-8') as f:
    file_content = f.read()
    urls = re.findall("POST.+HTTP/1.1|GET.+HTTP/1.1", file_content)
    dic = {}
    for url in urls:
        dic[url] = dic.get(url, 0) + 1
    t = zip(dic.values(), dic.keys())
    order = sorted(t, reverse=True)
    i = 0
    for o in order:
        if "css" in o[1] or "js" in o[1] or "png" in o[1] or "jpg" in o[1] or "gif" in o[1] or "mp4" in o[1]:
            continue
        elif i < 10:
            print(o)
            i = i + 1
        else:
            break



"""使用os模块实现 shell ls命令"""
import os
from pathlib import Path

def ls(directory_path):
    names = os.listdir(directory_path)
    for name in names:
        print(name)
        my_path = directory_path + '/' + name
        my_file = Path(my_path)
        if my_file.is_dir():
            sub_directory_path = my_path
            ls(sub_directory_path)

directory_path = r"/Users/jimmy/PycharmProjects/python_lesson"
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


