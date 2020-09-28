import numpy as np
import matplotlib.pyplot as plt

# 生成模拟数据
x = np.arange(0, 2*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制两条曲线
sin, = plt.plot(x, y1, 'r--')
cos, = plt.plot(x, y2, 'b-.')

# 创建第一个图例
legend1 = plt.legend([sin,cos],
                     ['sin','cos'],
                     loc='lower right')

x1 = np.random.randint(0, 6, 10)
x2 = np.random.randint(0, 6, 10)
y1 = np.random.randint(2, 5, 10)
y2 = np.random.randint(2, 5, 10)
# 绘制两个散点图
scatter1 = plt.scatter(x1, y1, s=20, c='r', marker='*')
scatter2 = plt.scatter(x2, y2, s=30, c='b', marker='v')

# 创建第二个图例
plt.legend([scatter1,scatter2],
           ['red scatter','blue scatter'],
           loc='lower right',
           bbox_to_anchor=(1, 0.5))
# 增加第一个图例
plt.gca().add_artist(legend1)

plt.show()
