from cmath import log
from math import pow
x = 0
h = 0.0001
a = 4 
for i in range(10):

    x = pow(a,h)-1

    b = x/h 
    
    h = h/10
    
    print(log(a))
    print(b)

