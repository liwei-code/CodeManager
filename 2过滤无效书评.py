comments = ['这是一本非常好的书，作者用心了',
            '作者大大辛苦了',
            '好书，感谢作者提供了这么多的好案例',
            '书在运输的路上破损了，我好悲伤。。。',
            '为啥我买的书上有菜汤。。。。',
            '啊啊啊啊啊啊，我怎么才发现这么好的书啊，相见恨晚',
            '书的质量有问题啊，怎么会开胶呢？？？？？？',
            '好好好好好好好好好好好',
            '好难啊看不懂好难啊看不懂好难啊看不懂',
            '书的内容很充实',
            '你的书上好多代码啊，不过想想也是，编程的书嘛，肯定代码多一些',
            '书很不错!!一级棒!!买书就上当当，正版，价格又实惠，让人放心!!! ',
            '无意中来到你小铺就淘到心意的宝贝，心情不错! ',
            '送给朋友的、很不错',
            '这是一本好书，讲解内容深入浅出又清晰明了，推荐给所有喜欢阅读的朋友同好们。']

##def rule(s):
##    return len(set(s))/len(s)>0.5
print(set(comments[5]))
rule = lambda s:len(set(s))/len(s)>0.5
result = filter(rule, comments)

print('原始书评：')
print(*comments, sep='\n')
##for comment in comments:
##    print(comment)

print('='*30)
print('过滤后的书评：')
for comment in result:
    print(comment)
