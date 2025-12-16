import matplotlib.pyplot as plt
import math as m

f = lambda x: x**2-2

a = 1
b = 2
r = m.sqrt(2)
tolerance = 0.0001

i = 1
root = []
error = []

while i<= 100:
    c = (a + b)/2
    root.append(c)

    err = abs(c-r)
    error.append(err)

    if err<tolerance:
        break
    print(f"Iter {i}, Root: {c:.6f}, Err: {err:.6f}")
    if(f(c)<0):
        a = c
    else:
        b = c

    i = i+1
plt.plot(root, label ='Root')
plt.plot(error, label = 'Error')
plt.legend()
plt.show()