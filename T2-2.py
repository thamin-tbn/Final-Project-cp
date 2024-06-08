import numpy as np
import matplotlib.pyplot as plt

#تعریف آرایه تعیین کننده خط به طول 50 و بار 1 و محل قرار گرفتن حرف O
x1 = ["1"  for _ in range(51)]
x2 = ["0"  for _ in range(51)]
x2[25]="O"
x=np.stack( (x1, x2),axis=1)

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
    # print(Q)     
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
        print(deltaX, deltaY )
    return Ex,Ey


Ex,Ey=efcal(x)