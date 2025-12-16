import matplotlib.pyplot as plt
import math as m

g = lambda x: m.sqrt(m.sin(x))

root = []
x0 = 1
for i in range (10):
    x1 = g(x0)
    root.append(x1)
    x0 = x1

plt.plot(root)
plt.xlabel('Iteration')
plt.ylabel('root')
plt.show()