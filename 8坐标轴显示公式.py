import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = np.sin(x)
plt.plot(x, y)
def func(num):
    pre, aft = f'{num:.2e}'.split('e')
    return f'${float(pre):.1f}x10^'+'{'+str(int(aft))+'}$'

plt.xticks(range(-10,12,3), list(map(func, range(-10,12,3))))
plt.yticks(np.arange(-1,1.1,0.25),
           list(map(func, np.arange(-1,1.1,0.25))))
plt.show()
