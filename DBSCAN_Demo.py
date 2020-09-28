import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs

def DBSCANtest(data, eps=0.6, min_samples=8):
    # 聚类
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(data)
        
    # 聚类标签（数组，表示每个样本所属聚类）和所有聚类的数量
    # 标签-1对应的样本表示噪点
    clusterLabels = db.labels_
    uniqueClusterLabels = set(clusterLabels)
    # 标记核心对象对应下标为True 
    coreSamplesMask = np.zeros_like(db.labels_, dtype=bool)
    coreSamplesMask[db.core_sample_indices_] = True
    # 绘制聚类结果
    colors = ['red', 'green', 'blue', 'gray', '#88ff66',
              '#ff00ff', '#ffff00', '#8888ff', 'black',]
    markers = ['v', '^', 'o', '*', 'h', 'd', 'D', '>', 'x']
    for label in uniqueClusterLabels:
        # 使用最后一种颜色和符号绘制噪声样本
        # clusterIndex是个True/False数组
        # 其中True表示对应样本为cluster类
        clusterIndex = (clusterLabels==label)
        
        # 绘制核心对象
        coreSamples = data[clusterIndex&coreSamplesMask]
        plt.scatter(coreSamples[:, 0], coreSamples[:, 1],
                    c=colors[label], marker=markers[label], s=100)

        # 绘制非核心对象
        nonCoreSamples = data[clusterIndex & ~coreSamplesMask]
        plt.scatter(nonCoreSamples[:, 0], nonCoreSamples[:, 1],
                    c=colors[label], marker=markers[label], s=20)
    plt.show()

data, labels = make_blobs(n_samples=300, centers=5)
DBSCANtest(data)
DBSCANtest(data, 0.8, 15)
