# 例  读取文本文件data.txt（文件中每行存放一个整数）中所有整数，按升序排序后再写入文本文件data_new.txt中。

with open('data.txt') as fp:
    data = fp.readlines()

data.sort(key=int)

with open('data_new.txt', 'w') as fp:
    fp.writelines(data)
