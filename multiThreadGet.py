import re
import requests
from bs4 import BeautifulSoup
from pybloom_live import ScalableBloomFilter
import csv
import jieba
import jieba.analyse
import time
import simhashCode
from queue import Queue
from threading import Thread
import threading
import distance
# 多线程同时爬取数据
def run(queue):
    while len(all_lst) > 0 and queue.empty() is not True:
        gLock.acquire()
        url = all_lst.pop(0)
        count = queue.get()
        gLock.release()
        print(count)
        if count == 20000:
            end = time.time()
            print("总耗时：",end - start)
            print("爬取网页完成，导入剩余url")
            length = len(all_lst)
            # 若all_list中剩余url，将其中没有保存的保存
            if length > 0:
                surplus_path = path + "\\surplusURL.csv"
                with open(surplus_path, 'w', encoding='utf-8') as fp:
                    wr = csv.writer(fp)
                    for i in range(length):
                        a = all_lst.pop(0)
                        if a in sbf:
                            continue
                        else:
                            sbf.add(a)
                            wr.writerow([str(count), a])
                            count += 1
        if url in sbf:
            continue
        url_lst = get_url(url, count)
        gLock.acquire()
        if len(url_lst) != 0:
            all_lst.extend(url_lst)
        sbf.add(url)
        gLock.release()


# 通过url获取html
def get_html(url):
    # 将爬取网页时的异常抛出去，防止中断爬取
    try:
        resp = requests.get(url, headers=head, timeout=1)
        if resp.status_code == 200:
            resp.encoding = resp.apparent_encoding
            return resp.text
        else:
            return ''
    except:
        print("request error")
        return ''


# 通过html，获取其中所有的url
def get_url(url, current):
    lst = []
    html = get_html(url)
    if html == '' or html == None:
        # print(url)
        return lst
    new_path = path + '\\' + str(current) + '.csv'
    new_text_path = text_path + '\\' + str(current) + '.csv'
    # 将匹配html的异常抛出去，防止中断爬取
    try:
        text = get_text(html)
        if len(text) > 30:
            text_list = jieba.cut(text)
            jieba.analyse.set_stop_words(r'E:\搜索引擎\哈工大停用词表.txt')
            keyWord = jieba.analyse.extract_tags('|'.join(text_list), topK=20, withWeight=True)
            simhash = simhashCode.simhash(keyWord)
            gLock.acquire()
            isRepeat = findSameHash(simhash)
            gLock.release()
            if isRepeat:
                print("相似")
                return lst
            with open(new_text_path, 'w', encoding='utf-8') as fp:
                    # 创建csv文件写入对象
                wr = csv.writer(fp)
                wr.writerow([keyWord])
    except Exception:
        print(Exception.args)
        print("findSameHash error")
        return lst
    try:
        with open(new_path, 'w', encoding='utf-8') as fp:
            # 创建csv文件写入对象
            wr = csv.writer(fp)
            wr.writerow(['url', url])
            wr.writerow(['html', html])
        # 匹配html中url
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('a', attrs={'href': re.compile('^http')})
    except Exception:
        print(Exception.args)
        return []
    for i in a:
        lst.append(i['href'])
    return lst


# 获取html中的正文
def get_text(html):
    html = html.encode('utf-8', 'ignore').decode("utf-8", "ignore")
    # 移除conten中的空行以及英文字母
    r = re.compile(r'^\s+$', re.M | re.S)  # 匹配全是字符的行,^表示从头开始bai匹配，$表示匹配到最后一du个字符
    # 替换
    s = r.sub('', html)
    # 匹配一个空行
    r = re.compile(r'\n+', re.M | re.S)
    s = r.sub('', s)
    # 移除html中的script,style,meta,注释等脚本
    r = re.compile(r'<script.*?</script>', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<style.*?</style>', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<img.*?</img>', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<!--.*?-->', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<meta.*?>', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<ins.*?</ins>', re.I | re.M | re.S)
    s = r.sub('', s)
    s = re.sub(r'<[^>]+>', '', s)
    # r = re.compile(r'\s|\t', re.I | re.M | re.S)
    # s = r.sub('', s)
    s = re.sub('\s|\t', '', s)
    # 过滤文本中的其他字符（除中文和数字之外）
    s = re.sub('[a-zA-Z’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", s)
    return s

# 抽屉原理，分别比较四段hash值，确定是否存在重复
def findSameHash(simhash):
    # 对比第一个hash表，第0-15位hash值
    num = int(simhash[:16],2)
    if len(hash1[num]) == 0:
        hash1[num].append(simhash)
    else:
        for i in range(len(hash1[num])):
            if distance.hamming(simhash,hash1[num][i]) < 3:
                return True
    # 对比第二个hash表，第16-31位hash值
    num2 = int(simhash[16:32],2)
    if len(hash2[num2]) == 0:
        hash2[num2].append(simhash)
    else:
        for i in range(len(hash2[num2])):
            if distance.hamming(simhash,hash2[num2][i]) < 3:
                return True
    # 对比第三个hash表，第32-47位hash值
    num3 = int(simhash[32:47],2)
    if len(hash3[num3]) == 0:
        hash3[num3].append(simhash)
    else:
        for i in range(len(hash3[num3])):
            if distance.hamming(simhash,hash3[num3][i]) < 3:
                return True
    # 对比第四个hash表，第48-63位hash值
    num4 = int(simhash[48:64],2)
    if len(hash4[num4]) == 0:
        hash4[num4].append(simhash)
    else:
        for i in range(len(hash4[num4])):
            if distance.hamming(simhash,hash4[num4][i]) < 3:
                return True
    return False



if __name__ == '__main__':
    # 设置种子URL
    url = r'https://www.sina.com.cn/'
    # 设置储存路径
    path = r'E:\url1'
    text_path = r'E:\text1'
    gLock = threading.Lock()
    queue = Queue()
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    all_lst = []
    # 初始化布隆过滤器，设置容器大小为100000
    sbf = ScalableBloomFilter(initial_capacity=100000, error_rate=0.001, mode=ScalableBloomFilter.LARGE_SET_GROWTH)
    # 将种子url设置为已爬取
    sbf.add(url)
    hash1 = []
    hash2 = []
    hash3 = []
    hash4 = []
    # 设置四个hash表保存simhash的四段值，每个hash表长度为10000
    for i in range(65536):
        hash1.append([])
        hash2.append([])
        hash3.append([])
        hash4.append([])
    count = 0
    # 爬取种子url中的url
    url_lst = get_url(url, 0)
    # with open(r'E:\url\surplusURL.csv', encoding='utf-8') as fp:
    #     for line in csv.reader(fp):
    #         if line:
    #             all_lst.append(line[1])
    all_lst.extend(url_lst)
    # 设置爬取网页的编号以及爬取数量
    for i in range(1, 20001):
        queue.put(i)
    # 开始计时，爬取数据时间
    start = time.time()
    # 使用多线程进行数据爬取
    for i in range(10):
        thread = Thread(target=run, args=(queue,))
        # thread.daemon = True  # 随主线程退出而退出
        thread.start()
