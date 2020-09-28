def demo(lst, k):
    #切片，以免影响原来的数据
    t_lst = lst[:]    
    #游戏一直进行到只剩下最后一个人
    num = len(t_lst)
    for i in range(num-1):
        for j in range(k-1):
            t_lst.append(t_lst.pop(0))
        t_lst.pop(0)        
    #游戏结束
    return t_lst[0]

lst = list(range(1,11))
print(demo(lst, 3))
