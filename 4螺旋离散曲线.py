from math import sin, cos
import numpy as np
import matplotlib.pyplot as plt
 
r = 20
# 绘制4个圆周
theta = np.arange(0, 8*np.pi, 0.1)
for t in theta:
    x = r*cos(t)
    y = r*sin(t)
    # 只绘制顶点
    plt.plot(x, y, 'ro')
    # 增加半径
    r = r+1

plt.gca().set_aspect('equal')
plt.show()
