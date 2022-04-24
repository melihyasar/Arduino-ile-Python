import matplotlib.pyplot as plt
from drawnow import drawnow
from random import randint
import numpy as np
import math
#---------çember oluşturmak için------------------
theta=np.linspace(0,np.pi,50)#0 ile pi arasını (180 derecelik açıyı) 50 parçaya bölüyor.ne kadar fazla parçaya bölerse çember o kadar düzgün olur
radius=80#çemberin çapı
cember_a=radius*np.cos(theta)
cember_b=radius*np.sin(theta)
#--------------------------------------
def x_y_bul(aci,hipotenus):
    if aci>90:
     aci=180-aci
     x_yon=-1
    else:
     x_yon=1
    x=hipotenus*math.cos(math.radians(aci))*x_yon
    y=hipotenus*math.sin(math.radians(aci))
    return x,y
#-------------------------------
plt.ion()#mathplotlibi interaktif moda alıyor.drawnow kütüphanesinin çalışması için gerekli

#-----------------------------
def makefig():
    plt.plot(cember_a,cember_b,color="blue")
    plt.plot([-80,80],[-0.3,-0.3],color="blue")
    plt.plot([0,x1],[0,y1],color="blue")
    plt.scatter(x_list,y_list,color="red") 
n=0
x_list=np.array([])
y_list=np.array([])
while True:
    print(1)
    m=randint(0,20)
    if m==12:
        h=randint(0,80)
        x,y=x_y_bul(n,h)
        x_list=np.append(x_list,x)
        y_list=np.append(y_list,y)
    x1,y1=x_y_bul(n,80)
    drawnow(makefig)
    n=n+2
    if n>180:
        n=0
        x_list=np.array([])
        y_list=np.array([])

    

