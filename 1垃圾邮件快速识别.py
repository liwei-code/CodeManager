def check(s1, s2):
    return sum(map(s1.count, s2))

print(check('这是一个测*#试邮#件，内】含广【告', '【】*#/\\'))
