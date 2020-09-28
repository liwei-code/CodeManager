import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

data = pd.DataFrame({'月份': [1,2,3,4,5,6,7,8,9,10,11,12],
              '男装': [51,32,58,57,30,46,38,38,40,53,58,50],
              '女装': [70,30,48,73,82,80,43,25,30,49,79,60],
              '餐饮': [60,40,46,50,57,76,70,33,70,61,49,45],
              '化妆品': [110,75,130,80,83,95,87,89,96,88,86,89],
              '金银首饰': [143,100,89,90,78,129,100,97,108,152,96,87]})

# 绘制柱状图，指定月份数据作为x轴
data.plot(x='月份', kind='bar')
# 设置x、y轴标签和字体
plt.xlabel('月份', fontproperties='simhei')
plt.ylabel('营业额（万元）', fontproperties='simhei')
# 设置图例字体
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf')
plt.legend(prop=myfont)

plt.show()
