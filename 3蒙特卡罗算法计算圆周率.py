from random import random

def estimatePI(times):
    hits = 0
    for i in range(times):
        x = random()*2 - 1
        y = random()*2 - 1
        if x*x + y*y <= 1:
            hits += 1
    return 4.0 * hits/times

print(estimatePI(10000))
print(estimatePI(1000000))
print(estimatePI(100000000))
