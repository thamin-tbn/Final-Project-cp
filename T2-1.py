import numpy as np
import matplotlib.pyplot as plt

#تعریف آرایه
x=np.array([["1","2","O"],["1","0","1"],["1","3","1"]])

# ذخیره بارها و مختصات آنها در لیست Qو برگرداندن مختصات نقطه O
def f1(x):
    a,b=x.shape
    Q=[]
    for i in range(a):
        for j in range(b):
          if x[i][j]!="O":
           Q.append((i,j,int(x[i][j])))  
          else:
           xx=i
           yy=j
           
    return Q,xx,yy

# محاسبه میدان الکتریکی در مختصات نقطه O
def efcal(x):
    
    Q,xx,yy=f1(x)       
    k = 9 * 10**9
    xp, yp = xx, yy
    Ex=0
    Ey=0
    for q in Q:
        deltaX = xp - q[0]
        deltaY = yp - q[1] 
     
        distance = (deltaX**2 + deltaY**2)**0.5 
    
        E = (k*q[2])/(distance**2)     
        Ex += E*(deltaX/distance)
        Ey += E*(deltaY/distance) 
    return Ex,Ey


Ex,Ey=efcal(x)