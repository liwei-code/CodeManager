import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 模拟数据
N = 25
df = pd.DataFrame({'一班':np.random.randint(1,100,N),
                   '二班':np.random.randint(1,100,N),
                   '三班':np.random.randint(1,100,N)})

# 折线图
df.plot()
myfont = fm.FontProperties(fname=r'C:\Users\肖诗川\Downloads\STKAITI.ttf')
plt.legend(prop=myfont)

# 柱状图
df.plot(kind='bar')
plt.legend(prop=myfont)

# 热力图
plt.figure()
plt.xticks(fontproperties='simhei')
sns.heatmap(df)

# 显示图形
plt.show()
