import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 读取文件中的数据
with open(r'商场一楼手机信号强度.txt', encoding='utf-8-sig') as fp:
    for line in fp:
        # print(line)
        x, y, s = map(int, line.split(','))
        # 绘制散点图，s指大小，c指颜色，marker指符号形状
        if s < 40:
            color = 'r'
        elif s < 70:
            color = 'b'
        else:
            color = 'g'
        plt.scatter(x, y, s=s*10, c=color, marker='*')

plt.xlabel('长度坐标',
            fontproperties='simhei',   # 设置中文字体
            fontsize=10)                 # 设置字号
plt.ylabel('宽\n度\n坐\n标',           # 每行显示一个字
            fontproperties='microsoft yahei',
            fontsize=14,
            rotation='horizontal')      # 设置文字方向
plt.title('商场内信号强度',
           fontproperties=fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf'),
           fontsize=14)

plt.show()
