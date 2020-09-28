from time import time
from os import listdir
from os.path import basename
from PIL import Image
from sklearn import svm
from sklearn.model_selection import cross_val_score,\
     ShuffleSplit, LeaveOneOut

# 图像尺寸
width, height = 30, 60

def loadDigits(dstDir='datasets'):
    # 获取所有图像文件名
    digitsFile = [dstDir+'\\'+fn for fn in listdir(dstDir)
                   if fn.endswith('.jpg')]
    # 按编号排序
    digitsFile.sort(key=lambda fn: int(basename(fn)[:-4]))
    # digitsData用于存放读取的图片中数字信息
    # 每个图片中所有像素值存放于digitsData中的一行数据
    digitsData = []
    for fn in digitsFile:
        with Image.open(fn) as im:
            data = [sum(im.getpixel((w,h)))/len(im.getpixel((w,h)))
                     for w in range(width)
                     for h in range(height)]
            digitsData.append(data)
    # digitsLabel用于存放图片中数字的标准分类
    with open(dstDir+'\\digits.txt') as fp:
        digitsLabel = fp.readlines()
    digitsLabel = [label.strip() for label in digitsLabel]
    return (digitsData, digitsLabel)

# 加载数据
data = loadDigits()
print('数据加载完成。')

# 创建模型
svcClassifier = svm.SVC(kernel="linear", C=1000, gamma=0.001)

# 交叉验证
start = time()
scores = cross_val_score(svcClassifier, data[0], data[1], cv=8)
print('交叉验证（k折叠）得分情况：\n', scores)
print('平均分：\n', scores.mean())
print('用时（秒）：', time()-start)
print('='*20)

start = time()
scores = cross_val_score(svcClassifier, data[0], data[1],
                           cv=ShuffleSplit(test_size=0.3,
                                             train_size=0.7,
                                             n_splits=10))
print('交叉验证（随机拆分）得分情况：\n', scores)
print('平均分：\n', scores.mean())
print('用时（秒）：', time()-start)
print('='*20)

start = time()
scores = cross_val_score(svcClassifier, data[0], data[1],
                           cv=LeaveOneOut())
print('交叉验证（逐个测试）得分情况：\n', scores)
print('平均分：\n', scores.mean())
print('用时（秒）：', time()-start)
