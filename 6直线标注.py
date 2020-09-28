import matplotlib.pyplot as plt

def onMouseDown(event):
    if event.button == 1:
        # 单击鼠标左键，绘制新直线，记录直线起点坐标
        global x0, y0
        x0 = event.xdata
        y0 = event.ydata

def onMouseMove(event):
    global x1, y1
    x1 = event.xdata
    y1 = event.ydata
    # 改进，如果鼠标不在当前图形中，直接返回
    if not (x1 and y1):
        return
    if event.button==1:
        # 删除最后绘制的一条直线
        if len(ax.lines)>1:
            del ax.lines[-1]
        # 从起点到当前位置绘制一条直线
        plt.plot([x0,x1], [y0,y1], c='r', lw=2)
        # 更新标注对象的当前位置
        annot.xy = (x1, y1)
        # 计算并显示当前位置与按下鼠标的位置的距离
        distance = ((x0-x1)**2 + (y0-y1)**2) ** 0.5
        distance = round(distance, 2)
        annot.set_text(str(distance))
        # 设置标注对象可见
        annot.set_visible(True)
        event.canvas.draw()

def onMouseUp(event):
    # 隐藏标注对象
    annot.set_visible(False)
    if event.button == 1:
        # ax.lines.clear()
        plt.plot([x0,x1], [y0,y1], c='r', lw=2)
        event.canvas.draw()
        
# 创建图形
fig = plt.figure()
ax = plt.gca()
im = plt.imread('sample.jpg')
plt.imshow(im)

# 创建标注对象
annot = ax.annotate("",
                    xy=(0,0),              # 箭头位置
                    xytext=(-10,10),       # 文本相对位置
                    # 相对于xy的偏移量单位
                    textcoords="offset pixels")
annot.set_visible(False)

# 设置响应并处理事件的函数
fig.canvas.mpl_connect('button_press_event', onMouseDown)
fig.canvas.mpl_connect('motion_notify_event', onMouseMove)
fig.canvas.mpl_connect('button_release_event', onMouseUp)

plt.show()
