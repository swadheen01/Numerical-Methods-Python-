import math as m
import matplotlib.pyplot as plt

#f = lambda x: m.exp(-x)-x
# df = lambda x: -m.exp(-x)-1
#x0= 0
# # iter =1
# while iter<=10:
#     x1 = f(x0)
#     # x1 = x0 -f(x0)/df(x0)
#     # c = b- (f(b)*(b-a))/(f(b)-f(a))
#     # err = abs(x1-x0)
#     # print(f"{iter} App_root : {x1} Abs_err: {err}")
#     x0=x1
    
#     iter= iter +1

g= lambda x: m.exp(-x)
x0=0
root =[]
err = []
for i in range (15):
    x1=g(x0)
    root.append(x1)
    err.append(abs(x0-x1))
    x0=x1
#plt.plot(root)
#plt.show()
#plt.plot(err)
#plt.xlabel("Iteration")
#plt.ylabel("Error")
#plt.show()*/
g2 = lambda x: m.exp(-x)
x = [i for i in range(100)]
y = [g2(p) for p in x]
plt.plot(x,y)
plt.show()
