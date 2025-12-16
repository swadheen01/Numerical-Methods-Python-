#
#Copyright (c) Swadheen Islam Robi (SIR01)
#Created on Tue Dec 09 2025 3:33:45 PM
#

import math as m 

f=lambda x: m.exp(x)
a=0
b=1
n=4
h=(b-a)/n

sum = (f(a)+f(b))/2

for i in range(n-1):
    a=a+h
    sum=sum+(f(a))
    
sum = sum*h
print(sum)



# import math as m 

# f=lambda x: m.exp(x)

# n=10
# a=0
# b=1

# h=(b-a)/n
# sum= f(a)+f(b)

# for i in range (1,n):
#     a = a+h
#     if i%2==0:
#         sum=sum+(2*f(a))
#     else:
#         sum=sum+(4*f(a))
        
# sum = sum*(h/3)
# print(sum)


# import math as m 
# f = lambda x:x**2+1

# a=0
# b=1
# n=12
# h=(b-a)/n

# sum = f(a)+f(b)

# for i in range (1,n):
#     a=a+h 
#     if i%3==0:
#         sum=sum+(3*f(a))
        
#     else :
#         sum=sum+(3*f(a))
# sum=sum*3*h/8
# print(sum)
# import math
# f = lambda x: math.exp(x)
# a = 0
# b = 1
# n = 12
# h = (b - a) / n

# sum = 0
# x0 = 0
# for i in range(2):              # two Weddle panels: 0-6 and 6-12
    
#     x1 = x0 + h
#     x2 = x1 + h
#     x3 = x2 + h
#     x4 = x3 + h
#     x5 = x4 + h
#     x6 = x5 + h
    
#     sum += (3*h/10) * (f(x0) + 5*f(x1) + f(x2) + 6*f(x3) + f(x4) + 5*f(x5) + f(x6))
#     x0 = x6

# print(sum)
