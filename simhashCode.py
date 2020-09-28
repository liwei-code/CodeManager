# -*- coding: utf-8 -*-
import jieba
import jieba.analyse
import numpy as np
import distance

# class simhash:
#     def __init__(self, content):
#         self.simhash = self.simhash(content)
#
#     def __str__(self):
#         return self.simhash

def simhash(keyWord):
    keyList = []
    # print(keyWord)
    for feature, weight in keyWord:
        weight = int(weight * 20)
        feature = string_hash(feature)
        temp = []
        for i in feature:
            if (i == '1'):
                temp.append(weight)
            else:
                temp.append(-weight)
            # print(temp)
        keyList.append(temp)
    list1 = np.sum(np.array(keyList), axis=0)
    if (keyList == []):  # 编码读不出来
        return '00'
    simhash = ''
    for i in list1:
        if (i > 0):
            simhash = simhash + '1'
        else:
            simhash = simhash + '0'
    return simhash


def string_hash( source):
    if source == "":
        return 0
    else:
        x = ord(source[0]) << 7
        m = 1000003
        mask = 2 ** 128 - 1
        for c in source:
            x = ((x * m) ^ ord(c)) & mask
        x ^= len(source)
        if x == -1:
            x = -2
        x = bin(x).replace('0b', '').zfill(64)[-64:]

        return x

    '''
    以下是使用系统自带hash生成，虽然每次相同的会生成的一样，
    不过，对于不同的汉子产生的二进制，在计算海明码的距离会不一样，
    即每次产生的海明距离不一致
    所以不建议使用。
    '''
    # x=str(bin(hash(source)).replace('0b','').replace('-','').zfill(64)[-64:])
    # print(source,x,len(x))
    # return x


def hammingDis(a, b):
    t1 = '0b' + a
    t2 = '0b' + b
    n = int(t1, 2) ^ int(t2, 2)
    i = 0
    while n:
        n &= (n - 1)
        i += 1
    return i


# 比较不同的个数
# def distance_post_simhash(simhash_value1, simhash_value2, f=64):
#     x = (simhash_value1 ^ simhash_value2) & ((1 << f) - 1)
#     ans = 0
#     while x:
#         ans += 1
#         x &= x - 1
#     return ans

# def isRepeat(simhash_value,simhash_lst):
#     length = len(simhash_lst)
#     if length == 0:
#         return False
#     else:
#         flag = 0
#         for i in range(length):
#             simhash_value2 = simhash_lst[i]
#             num = 0
#             for j in range(0,4):
#                 distance = distance_post_simhash(simhash_value[j*16:(j+1)*16],simhash_value2[j*16:(j+1)*16])
#                 if distance == 0:
#                     return True


# str = "传统两个文本相似性的方法，大多是将文本分词之后，转化为特征向量距离的度量，比如常见的欧氏距离、海明距离或者余弦角度等等。两两比较固然能很好地适应，但这种方法的一个最大的缺点就是，无法将其扩展到海量数据。例如，试想像Google那种收录了数以几十亿互联网信息的大型搜索引擎，每天都会通过爬虫的方式为自己的索引库新增的数百万网页，如果待收录每一条数据都去和网页库里面的每条记录算一下余弦角度，其计算量是相当恐怖的。"
# str2 = "传统比较两个文本相似性的做法，大多是将文本分词之后，转化为特征向量距离的度量，比如常见的欧氏距离、海明距离或者余弦角度等等。两两比较固然能很好地适应，但这种方法的一个最大的缺点就是，无法将其扩展到海量数据。例如，试想像Google那种收录了数以几十亿互联网信息的大型搜索引擎，每天都会通过爬虫的方式为自己的索引库新增的数百万网页，如果待收录每一条数据都去和网页库里面的每条记录算一下余弦角度，其计算量是非常恐怖的。"
# str3 = '你妈妈喊你回家吃饭哦，回家罗回家罗'
# str4 = '你妈妈叫你回家吃饭啦，回家罗回家罗'
# seg1 = jieba.cut(str)
# jieba.analyse.set_stop_words(r'E:\搜索引擎\哈工大停用词表.txt')
# keyWord1 = jieba.analyse.extract_tags(
#     '|'.join(seg1), topK=10, withWeight=True, allowPOS=())
# print(keyWord1)
# seg2 = jieba.cut(str2)
# jieba.analyse.set_stop_words(r'E:\搜索引擎\哈工大停用词表.txt')
# keyWord2 = jieba.analyse.extract_tags(
#     '|'.join(seg2), topK=10, withWeight=True, allowPOS=())
# print(keyWord2)
# ha1 = simhash(keyWord1)
# ha2 = simhash(keyWord2)
# print(ha1)
# print(int(ha1[0:16]))
# print(int(ha1[0:16],2))
# print(ha2)
# i= distance.hamming(ha1,ha2)
# print(i)
# print(ha1)
# print(ha2)
# distance_post_simhash(int(t1,2), int(t2,2))
