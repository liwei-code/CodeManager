import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 每月支出数据
data = {
  '蔬菜': [1350,1500,1330,1550,900,1400,980,1100,1370,1250,1000,1100],
  '水果': [400,600,580,620,700,650,860,900,880,900,600,600],
  '肉类': [480,700,370,440,500,400,360,380,480,600,600,400],
  '日用': [1100,1400,1040,1300,1200,1300,1000,1200,950,1000,900,950],
  '衣服': [650,3500,0,300,300,3000,1400,500,800,2000,0,0],
  '旅游': [4000,1800,0,0,0,0,0,4000,0,0,0,0],
  '随礼': [0,4000,0,600,0,1000,600,1800,800,0,0,1000]
}

dataLength = len(data['蔬菜'])         # 数据长度
print(dataLength)
# angles数组把圆周等分为dataLength份
angles = np.linspace(0,                # 数组第一个数据
                       2*np.pi,          # 数组最后一个数据
                       dataLength,       # 数组中数据数量
                       endpoint=False)   # 不包含终点

markers = '*v^Do'
for col in data.keys():
    # 使用随机颜色和标记符号
    color = '#'+''.join(map('{0:02x}'.format,
                               np.random.randint(0,255,3)))
    print(color)
    plt.polar(angles, data[col], color=color,
               marker=random.choice(markers), label=col)
    
# 设置角度网格标签
plt.thetagrids(angles*180/np.pi,
                list(map(lambda i:'%d月'%i, range(1,13))),
                fontproperties='simhei')

# 创建和设置图例字体
font = fm.FontProperties(fname=r'C:\Users\肖诗川\Downloads\STKAITI.ttf')
plt.legend(prop=font)

plt.show()
