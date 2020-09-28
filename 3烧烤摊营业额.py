import matplotlib.pyplot as plt

#月份和每月营业额
month = list(range(1,13))
money = [5.2, 2.7, 5.8, 5.7, 7.3, 9.2,
         18.7, 15.6, 20.5, 18.0, 7.8, 6.9]
# plot()函数的第一个参数表示横坐标数据，第二个参数表示纵坐标数据
# 第三个参数表示颜色、线型和标记样式
# 颜色常用的值有（r/g/b/c/m/y/k/w）
# 线型常用的值有（-/--/:/-.）
# 标记样式常用的值有（./,/o/v/^/s/*/D/d/x/</>/h/H/1/2/3/4/_/|）
plt.plot(month, money, 'r-.v')

plt.xlabel('月份', fontproperties='simhei', fontsize=14)
plt.ylabel('营业额（万元）', fontproperties='simhei', fontsize=14)
plt.title('烧烤店2019年营业额变化趋势图',
           fontproperties='simhei', fontsize=18)

# 紧缩四周空白，扩大绘图区域可用面积
plt.tight_layout()

plt.show()
