import csv
import random
import datetime

fn = r'E:\url\date.csv'

with open(fn, 'w',encoding='utf-8') as fp:
    # 创建csv文件写入对象
    wr = csv.writer(fp)
    # 写入表头
    wr.writerow(['日期', '销量'])

    # 把今天作为模拟数据的第一天
    startDate = datetime.date.today()

    # 生成模拟数据，可以根据需要进行调整数量
    for i in range(1, 300):
        # 生成一个模拟数据，写入csv文件
        amount = 300 + i*5 + random.randrange(100)
        wr.writerow([str(startDate), amount])
        # 下一天
        startDate = startDate + datetime.timedelta(days=1)

# 读取并显示上面代码生成的csv文件内容
with open(fn) as fp:
    for line in csv.reader(fp):
        if line:
            print(*line)
