def climbStairs1(n):
    # 递推法
    a = 1
    b = 2
    c = 4
    for i in range(n-3):
        c, b, a = a+b+c, c, b # 序列解包
    return c

def climbStairs2(n):
    #递归法
    first3 = {1:1, 2:2, 3:4}
    if n in first3.keys():
        return first3[n]
    else:
        return climbStairs2(n-1) +  climbStairs2(n-2) +  climbStairs2(n-3)

print(climbStairs1(15))
print(climbStairs2(15))
