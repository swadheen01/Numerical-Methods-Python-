
import matplotlib.pyplot as plt
#gauss jacobi
#gauss seidel hole x1, y1 hobe na
#2x + y = 3, x - 3y = -5

x = 0
y = 0

solX=[]
solY = []
for i in range(15):
    x1 = (3-y)/2
    y1 = (x+5)/3
    solX.append(x1)
    solY.append(y1)
    x = x1
    y = y1


plt.plot(solX)
plt.plot(solY)

plt.xlabel('Iteration')
plt.ylabel('Solution')

plt.legend()
plt.show()

