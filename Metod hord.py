#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.misc import derivative
import numpy as np


# In[2]:


def f(x):
    return x**4 + np.exp(-x)


# In[3]:


print("Введите погрешность")
eps = float(input())
print("Введите a и b")
a = float(input())
b = float(input())
k=0
yk=a - (derivative(f,a, dx=0.001)/(derivative(f,a, dx=0.001)-derivative(f,b, dx=0.001))) * (a - b)
print('y0 = ', yk)
while (abs(derivative(f,yk, dx=0.001)) > eps):
    if derivative(f,yk, dx=0.001) > 0:
        b = yk
    else:
        a =yk
    yk=a - (derivative(f,a, dx=0.001)/(derivative(f,a, dx=0.001)-derivative(f,b, dx=0.001))) * (a - b)
    k+=1
    print('y',k, '=', yk, sep='')
print("При погрешности", eps, 'функция достигает своего минимума в точке', yk)
print("Её значение там", f(yk))


# In[ ]:




