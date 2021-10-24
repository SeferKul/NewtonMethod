#!/usr/bin/env python
# coding: utf-8

# In[16]:


import sympy as sym

def func(b):  #calculating first derivative of the function
    x=sym.Symbol('x')
    d=(x**7)-1000
    return d.subs(x,b)

def fderfunc(c):  #calculating second derivative of the function
    x=sym.Symbol('x')
    der=sym.diff((x**7)-1000)
    return der.subs(x,c)

def newtonmthd():
    Eps=float(input('enter Eps value:')) #value request part
    v0=float(input('enter v0 value:'))
    v1=v0-(func(v0)/fderfunc(v0))
    i=1

    while (abs(v1-v0))>Eps and abs(fderfunc(v1))>Eps:#controlling part
        v0=v1
        v1=v0-(func(v0)/fderfunc(v0)) #calculation
        i=i+1
    print('iteration no:',i)   
    return(v1)
x=newtonmthd()

print(x)


# In[ ]:





# In[ ]:




