import matplotlib.pyplot as plt
import math as m

f = lambda x: m.cos(x) - 3*x + 1
df = lambda x: - m.sin(x) - 3



root = []
x0 = 0.5
for i in range (10):
    x1 = x0- f(x0)/df(x0)
    root.append(x1)
    err = abs(x1-x0)
    print("Iter num: %d, err: %0.5f, Root: %0.5f" %(i, err, x1))
    x0 = x1

plt.plot(root)
plt.xlabel('Iteration')
plt.ylabel('root')
plt.show()