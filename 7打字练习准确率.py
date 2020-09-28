def Rate1(origin, userInput):
    if not (isinstance(origin, str) and isinstance(userInput, str)):
        print('The two parameters must be strings.')
        return
    if len(origin)<len(userInput):
        print('Sorry. I suppose the second parameter string is shorter.')
        return    
    right = 0                   #精确匹配的字符个数
    for origin_char, user_char in zip(origin, userInput):
        if origin_char==user_char:
            right += 1
    return right/len(origin)

def Rate2(origin, userInput):
    '''使用生成器表达式'''
    if not (isinstance(origin, str) and isinstance(userInput, str)):
        print('The two parameters must be strings.')
        return
    if len(origin)<len(userInput):
        print('Sorry. I suppose the second parameter string is shorter.')
        return    
    right = sum((1 for oc, uc in zip(origin, userInput) if oc==uc))
    return right/len(origin)

def Rate3(origin, userInput):
    '''函数式编程'''
    if not (isinstance(origin, str) and isinstance(userInput, str)):
        print('The two parameters must be strings.')
        return
    if len(origin)<len(userInput):
        print('Sorry. I suppose the second parameter string is shorter.')
        return    
    right = sum(map(lambda oc, uc:oc==uc, origin, userInput))
    return right/len(origin)


origin = 'Shandong Institute of Business and Technology'
userInput = 'ShanDong institute of business and technolog'
print(Rate1(origin, userInput))   #输出测试结果
print(Rate2(origin, userInput))   #输出测试结果
print(Rate3(origin, userInput))   #输出测试结果