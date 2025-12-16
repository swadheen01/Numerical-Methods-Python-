import math as m
import matplotlib.pyplot as plt

x = 0
y = 0
z = 0

i = 1
XX = [x]
while i<=5:
    x = (9-2*y-z)/10
    y = (19-2*x-3*z)/10
    z = (0-x-3*y)/10
    XX.append(x)
    i = i+1
print(x)
print(y)
print(z)
plt.plot(XX)
plt.xlabel('Iteration')
plt.ylabel('X value')
plt.show()
