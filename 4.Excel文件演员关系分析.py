from itertools import combinations
from functools import reduce
import openpyxl
from openpyxl import Workbook

def getActors(filename):
    actors = dict()
    # 打开xlsx文件，并获取第一个worksheet
    wb = openpyxl.load_workbook(filename)
    ws = wb.worksheets[0]
    # 遍历Excel文件中的所有行
    for index, row in enumerate(ws.rows):
        # 绕过第一行的表头
        if index == 0:
            continue
        # 获取电影名称和演员列表
        filmName, actor = row[0].value, row[2].value.split('，')
        # 遍历该电影的所有演员，统计参演电影
        for a in actor:
            actors[a] = actors.get(a, set()) | {filmName}
    return actors

data = getActors('电影导演演员.xlsx')
# 排序
actors = sorted(data.items(), key=lambda x:int(x[0][2:]))
for item in actors:
    print(item)

data = getActors('电影导演演员.xlsx')
def relations():
    # 演员名单
    actors = tuple(data.keys())
    trueLove = [0, '']
    # 选择法，共同参演电影数量最多的两个演员
    for index1, actor1 in enumerate(actors):
        for actor2 in actors[index1+1:]:
            common = len(data[actor1]&data[actor2])
            if common > trueLove[0]:
                trueLove = [common, (actor1, actor2)]

    return ('关系最好的两个演员是{0[1]}，'
            'Ta们共同主演的电影数量是{0[0]}'.format(trueLove))
print(relations())