import numpy as np
def simson(n):
    def f(x):
        return np.log(x)

    a=1
    b=5
    delx=(b-a)/n
    sum=(f(a)+f(b))*delx/3
    sum2=0
    

    for i in range(2,n-1,2):
    
        sum2+=2*f(a+i*delx)*delx/3
    sum3=0
    for i in range(1,n,2):
        sum3+=4*f(a+i*delx)*delx/3
    ans=(sum+sum2+sum3)
    return ans

print(simson(4))
