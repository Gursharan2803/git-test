import math
from matplotlib import pyplot as plt

def newtonrapson(x):
    def f(x):
        return x*x-10
    def df(x):
        return 2*x

    h=f(x)/df(x)
    list=[]
    list.append(h)
    while abs(h) >= math.exp(-6):
        h=f(x)/df(x)
            
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
        list.append(x)
    print(x)

    return list

x0=0.1
list=[]
list=newtonrapson(x0)
plt.plot(list)
plt.show()
