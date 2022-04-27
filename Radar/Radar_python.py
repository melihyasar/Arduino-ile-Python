import matplotlib.pyplot as plt
from drawnow import drawnow
import serial
import numpy as np
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
    x=hipotenus*np.cos(np.radians(aci))*x_yon
    y=hipotenus*np.sin(np.radians(aci))
    return x,y
#-------------------------------
plt.ion()#mathplotlibi interaktif moda alıyor.drawnow kütüphanesinin çalışması için gerekli
#-----------------------------
def makefig():
    plt.plot(cember_a,cember_b,color="blue")
    plt.plot([-80,80],[-0.3,-0.3],color="blue")
    plt.plot([0,x1],[0,y1],color="blue")
    plt.scatter(x_list,y_list,color="red")    
x_list=np.array([])
y_list=np.array([])
arduinoData=serial.Serial('COM5',19200)
while 1:
    try:
        arduinostring=arduinoData.readline()
        arduinolist=str(arduinostring).split(',')
        h=float(arduinolist[0].replace("b'",""))
        n=(arduinolist[1].replace("'",""))
        n=float(n.replace("\\r\\n",""))
        print(n,h)
        x,y=x_y_bul(n,h)
        if h!=0.0:       
            x_list=np.append(x_list,x)
            y_list=np.append(y_list,y)
        x1,y1=x_y_bul(n,80)
        drawnow(makefig)
        if n==0:
            x_list=np.array([])
            y_list=np.array([])
    except:
        print("error")
    

