import matplotlib.pyplot as plt
import numpy as np

# 生成模拟数据
x = np.arange(0, 2*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建图形，切分绘图区域，绘制两条曲线
fig = plt.figure(1)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
l1, = ax1.plot(x, y1, 'r--')
l2, = ax2.plot(x, y2, 'b-.')

# 设置并显示图例，使用bbox_to_anchor参数使图例显示于子图之外
plt.legend([l1, l2],                      # 需要显示图例的两条曲线
           ['sin curve', 'cos curve'],    # 图例中与两条曲线对应的文本
           loc='lower right',             # 图例右下角位置
           bbox_to_anchor=(1, 2.2))

plt.show()
