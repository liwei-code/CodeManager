from random import choice
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 散点数量
N = 100

# 创建图形和轴域
fig = plt.figure()
ax = plt.axes(xlim=(0,100), ylim=(10,100))
x = np.random.randint(10,90,N)
y = np.random.randint(20,90,N)
scatters = plt.scatter(x, y, marker='*', s=120)

def init():
    return scatters,

def update(i):
    # 对散点符号的颜色、大小、边线颜色进行调整和变化
    scatters.set_facecolor(np.random.random((N,3)))
    scatters.set_sizes(np.random.randint(50,200,N))
    scatters.set_edgecolors(np.random.random((N,3)))
    return scatters,

ani = FuncAnimation(fig=fig,       # 创建动画的图形
                    func=update,   # 用来更新图形的函数
                    frames=range(0,100,1), # update()函数的参数范围
                    init_func=init,# 初始化图形的函数
                    interval=500,  # 毫秒
                    blit=True)

ani.save('scatters.gif', writer='imagemagick')
