import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

# 生成测试数据
x = np.random.randint(0, 40, 30)
y = np.random.randint(0, 40, 30)
z = np.random.randint(0, 40, 30)

# 创建三维图形
ax = plt.subplot(projection='3d')
# 绘制三维柱状图
for xx, yy, zz in zip(x,y,z):
    color = 'r'
    if 10<zz<20:
        color = 'b'
    elif zz>=20:
        color = 'g'
    ax.scatter(xx, yy, zz, c=color, marker='*',
                s=160, linewidth=1, edgecolor='b')

# 设置坐标轴标签和图形标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('三维散点图', fontproperties='simhei', fontsize=24)

plt.show()
