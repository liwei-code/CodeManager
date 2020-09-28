import matplotlib.pyplot as plt

# 月份和每月营业额
month = list(range(1,13))
money = [5.2, 2.7, 5.8, 5.7, 7.3, 9.2,
         18.7, 15.6, 20.5, 18.0, 7.8, 6.9]

# 绘制每个月份的营业额
for x, y in zip(month, money):
    # 营业额越高，颜色中的红色分量越大
    # 格式字符串中的0表示不够2位时前面补0
    color = '#%02x'%int(y*10)+'6666'
    plt.bar(x, y,
            color=color, hatch='*', width=0.6,
            edgecolor='b', linestyle='--',linewidth=1.5)
    plt.text(x-0.3, y+0.2, '%.1f'%y)

# 设置x、y轴标签和字体
plt.xlabel('月份', fontproperties='simhei')
plt.ylabel('营业额（万元）', fontproperties='simhei')
plt.title('烧烤店营业额', fontproperties='simhei', fontsize=14)
    
# 设置x轴刻度
plt.xticks(month)

# 设置y轴跨度
plt.ylim(0, 22)

plt.show()
