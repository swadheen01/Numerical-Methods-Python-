import math as m
import matplotlib.pyplot as plt

f = lambda x: 5 * m.exp(x) - 6
df = lambda x: 5 * m.exp(x)

x0 = 1

i = 1
err = x0
tol = 0.00001
while i<=100:
    x1 = x0 - f(x0)/df(x0)
    error = abs(x1-x0)
    R_err = (abs(x1-x0)/x1)*100
    #print(err)
    if error<tol:
        break
    x0 = x1
    i+=1
print(x0)
print(R_err)