import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

ax1 = plt.subplot(241)
# 在子图中绘制极坐标图
ax2 = plt.subplot(242, projection='polar')
ax3 = plt.subplot(243, projection='polar')
# 设置polar=True，等价于设置projection='polar'
ax4 = plt.subplot(244, polar=True)
# 在子图中绘制三维图形
ax5 = plt.subplot(212, projection='3d')

# 紧缩四周空白，扩大绘图面积，设置子图之间的水平距离与垂直距离
plt.tight_layout()
plt.subplots_adjust(wspace=0.2, hspace=0.2)

# 测试数据
r = np.arange(1, 6, 1)
theta = (r-1) * (np.pi/2)
x = np.arange(1, 7, 0.5)
y = np.linspace(1, 3, 12)
z = 20*np.sin(x+y)

# 在不同子图中绘制图形
ax1.plot(theta, r, 'b--D')
ax2.plot(theta, r, linewidth=3, color='r')
ax3.scatter(theta, r, marker='*', c='g', s=60)
ax4.bar(theta, r)
ax5.plot(x, y, z)

plt.show()
