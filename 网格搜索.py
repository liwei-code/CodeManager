from time import time
from os import listdir
from os.path import basename
from PIL import Image
from sklearn import svm
from sklearn.model_selection import GridSearchCV

# 图像尺寸
width, height = 30, 60

def loadDigits(dstDir='datasets'):
    # 函数代码没有改变，此处省略，请参见上一节内容

# 加载数据
data = loadDigits()
print('数据加载完成。')

# 创建模型
svcClassifier = svm.SVC()
# 待测试的参数
parameters = {'kernel': ('linear', 'rbf'),
               'C': (0.001, 1, 10, 100, 1000),
               'gamma':(0.001, 0.1, 0.5, 1, 10)}


# 交叉验证
start = time()
clf = GridSearchCV(svcClassifier, parameters)
clf.fit(data[0], data[1])
# 解除注释可以查看详细结果
# print(clf.cv_results_)
print(clf.best_params_)
print('得分：', clf.score(data[0], data[1]))
print('用时（秒）：', time()-start)
