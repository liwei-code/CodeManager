import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建轴域，设置左、下边距和宽度、高度
ax1 = plt.axes([0.1, 0.15, 0.8, 0.3])
# 在轴域中绘制图形，保存绘制的曲线
l1, = ax1.plot(x, y1, 'r-', lw=2)
# 设置坐标轴标签，rotation控制文字旋转角度，0表示水平
ax1.set_xlabel('x', fontsize=14,
               # 坐标轴标签的位置
               position=(1,0))
ax1.set_ylabel('y', fontsize=14,
               rotation=0,
               position=(0,1))
# 轴域上侧和右侧坐标轴不可见
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
# 在轴域下方显示标题
plt.sca(ax1)
plt.title('sin curve', x=0, y=-0.35, fontsize=18)

# 图形中上半部分的轴域
ax2 = plt.axes([0.1, 0.6, 0.8, 0.3])
l2, = ax2.plot(x, y2, 'g--', lw=2)
ax2.set_xlabel('x', fontsize=14)
ax2.set_ylabel('y', fontsize=14, rotation=0)

# 创建图例
ax1.legend([l1,l2],  # 显示这两个曲线的图例
           # 每个曲线的图例文本
           ['sin curve', 'cos curve'],
           # 设置图例右下角位置
           loc='lower right',
           # 相对于轴域ax1的坐标
           bbox_to_anchor=(1,1.01))
# 在轴域下方显示标题
plt.sca(ax2)
plt.title('cos curve', x=0, y=-0.35, fontsize=18)

# 整个图形的标题
ax2.text(4, 1.2, 'sin-cos curve', fontsize=24)

# 显示图形
plt.show()
