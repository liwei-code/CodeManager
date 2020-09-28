import numpy as np
import matplotlib.pyplot as plt

# 某学生的课程与成绩
courses = ['C++', 'Python', '高数', '大学英语', '软件工程',
           '组成原理', '数字图像处理', '计算机图形学']
scores = [80, 95, 78, 85, 45, 65, 80, 60]

dataLength = len(scores)               # 数据长度

# angles数组把圆周等分为dataLength份
angles = np.linspace(0,                # 数组第一个数据
                     2*np.pi,          # 数组最后一个数据
                     dataLength,       # 数组中数据数量
                     endpoint=False)   # 不包含终点

scores.append(scores[0])
angles = np.append(angles, angles[0]) # 闭合
# 绘制雷达图
plt.polar(angles,                      # 设置角度
           scores,                      # 设置各角度上的数据          
           'rv--',                      # 设置颜色、线型和端点符号
           linewidth=2)                 # 设置线宽

# 设置角度网格标签
plt.thetagrids(angles*180/np.pi,
                courses,
                fontproperties='simhei')

# 填充雷达图内部
plt.fill(angles,
          scores,
          facecolor='r',
          alpha=0.3)

plt.show()
