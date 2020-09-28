import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 创建图形和轴域
fig = plt.figure()
ax = plt.axes(xlim=(0,100), ylim=(10,100))
x = []
y = []
line, = plt.plot(x, y)

def init():
    x.clear()
    y.clear()
    line.set_data(x, y) 
    return line,

def update(i):
    x.append(i)
    y.append(np.random.randint(30,80))
    line.set_data(x, y)            # 更新图形数据
    return line,

ani = FuncAnimation(fig=fig,       # 创建动画的图形
                    func=update,   # 用来更新图形的函数
                    frames=range(0,100,5), # update()函数的参数范围
                    init_func=init,# 初始化图形的函数
                    interval=500,  # 毫秒
                    blit=True)     # 更新所有顶点

ani.save('lines.gif', writer='imagemagick')
