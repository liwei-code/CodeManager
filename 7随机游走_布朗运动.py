import numpy as np
import matplotlib.pyplot as plt

# c表示散点的数量
r, c = 2, 80
# 散点初始位置
positions = np.random.randint(-10, 10, (r, c))
# 每个散点的颜色，随机彩色
colors = np.random.random((c,3))
while True:
    # 0.1秒刷新一次
    plt.pause(0.1)
    # 随机游走，更新每个散点的位置
    positions = positions+np.random.choice((1,-1), (r, c))
    positions = positions+np.random.choice((1,-1), (r,c))
    positions = np.where((positions>-39)&(positions<39),
                         positions, np.sign(positions)*39)
    # 下面两行是等价语句
    # positions[positions>39] = 39
    # positions[positions<-39] = -39
    plt.cla()
    # 重新绘制散点图
    scatters = plt.scatter(positions[0], positions[1],
                           marker='*', s=60, c=colors)
    plt.xlim(-40, 40)
    plt.ylim(-40, 40)
    
plt.show()
