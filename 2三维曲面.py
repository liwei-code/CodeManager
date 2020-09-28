import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

# 生成测试数据，在x和y方向分布生成-2到2之间的20个数
# 步长使用虚数，虚部表示点的个数，并且包含end
x, y = np.mgrid[-2:2:20j, -2:2:20j]
z = 50 * np.sin(x+y*2)

# 创建三维图形
ax = plt.subplot(111, projection='3d')
# 绘制三维曲面
ax.plot_surface(x,y,z,
                 rstride=3, cstride=2,
                 cmap=plt.cm.coolwarm)
# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# 设置图形标题
ax.set_title('三维曲面', fontproperties='simhei', fontsize=24)

plt.show()
