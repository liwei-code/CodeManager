import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fig = plt.figure(facecolor='red')
ax = fig.gca(facecolor='#ffaaee')
# 创建DataFrame结构
df = pd.DataFrame({'男性':(450,800,200),
                   '女性':(150,100,300)})
# 绘制柱状图
df.plot(kind='bar', ax=ax, color=['red','blue'])

# 设置x轴刻度和文本
plt.xticks([0,1,2],
           ['从不闯红灯', '跟从别人闯红灯', '带头闯红灯'],
           color='green',
           fontproperties='simhei',     # 中文字体
           rotation=20)                  # 旋转刻度的文本

# 设置y轴只在有数据的位置显示刻度
plt.yticks(list(df['男性'].values) + list(df['女性'].values))
plt.ylabel('人数', fontproperties='stkaiti', fontsize=14)
plt.title('过马路方式', fontproperties='stkaiti', fontsize=20)

# 创建和设置图例字体
font = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf')
plt.legend(prop=font)

plt.show()
