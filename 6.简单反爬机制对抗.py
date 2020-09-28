from re import findall
from urllib.parse import urljoin
from urllib.request import urlopen, Request

url = r'http://jwc.sdtbu.edu.cn/info/2002/5418.htm'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
           'Referer': url, }  # 不加这一项会有防盗链提示

req = Request(url=url, headers=headers)
with urlopen(req) as fp:
    content = fp.read().decode()

pattern = r'<a href="(.+?)"><span>(.+?)</span>'
for fileUrl, fileName in findall(pattern, content):
    if 'javascript' in fileUrl:
        continue
    fileUrl = urljoin(url, fileUrl)
    req = Request(url=fileUrl, headers=headers)
    with urlopen(req) as fp1:
        with open(fileName, 'wb') as fp2:
            fp2.write(fp1.read())
