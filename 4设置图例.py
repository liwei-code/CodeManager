import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

t = np.arange(0.0, 2*np.pi, 0.01)
s = np.sin(t)
c = np.cos(t)

plt.plot(t, s, label='正弦')
plt.plot(t, c, label='余弦')
plt.title('sin-cos函数图像',         #标题文本
           fontproperties='simhei',  #标题字体
           fontsize=24)               #标题字号
plt.xlabel('x坐标', fontproperties='simhei', fontsize=18)
plt.ylabel('正弦余弦值', fontproperties='simhei', fontsize=18)

myfont = fm.FontProperties(fname=r'C:\Users\肖诗川\Downloads\STKAITI.ttf')
plt.legend(prop=myfont,              #图例字体
            title='Legend',           #图例标题
            loc='lower left',         #图例左下角坐标为(0.43,0.75)
            bbox_to_anchor=(0.43,0.75),
            shadow=True,               #显示阴影
            facecolor='yellowgreen',  #图例背景色
            edgecolor='red',           #图例边框颜色
            ncol=2,                     #显示为两列
            markerfirst=False)         #图例文字在前，符号在后

plt.show()
