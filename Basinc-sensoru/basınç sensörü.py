import matplotlib.pyplot as plt
from drawnow import drawnow
import serial
import time
port=input("port numarası?")

print("Çalışma modu:")
print("0)Rakım")
print("1)Basınç")
print("2)Yerden yükseklik")
calisma_modu=int(input("? "))
if calisma_modu==0:
    i=input("Basınç?")
elif calisma_modu==1:
    i=input("Rakım?")
else:
    i="0"
port="COM"+port
plt.ion()#mathplotlibi interaktif moda alıyor.drawnow kütüphanesinin çalışması için gerekli
def makefig():
    if calisma_modu==0:
        plt.subplot(1, 2, 1)
        plt.ylim(p-10,p+10)
        plt.ylabel('Rakım(m),'+str(p))
        plt.xlabel('geçen süre(saniye)')
        plt.plot(sure,basinc,"bo-")
    elif calisma_modu==1:
        plt.subplot(1, 2, 1)
        plt.ylim(p-10,p+10)
        plt.ylabel('Basınç(hPa),'+str(p))
        plt.xlabel('geçen süre(saniye)')
        plt.plot(sure,basinc,"bo-")
    elif calisma_modu==2:
        plt.subplot(1, 2, 1)
        plt.ylim(p-10,p+10)
        plt.ylabel('Yerden yükseklik,'+str(p))
        plt.xlabel('geçen süre(saniye)')
        plt.plot(sure,basinc,"bo-")       
    plt.subplot(1, 2, 2)
    plt.ylim([t-3,t+3])
    plt.ylabel('sıcaklık(C),'+str(t))
    plt.xlabel('geçen süre(saniye)')
    plt.plot(sure,sicaklik,"ro-")
arduinoData=serial.Serial(port,19200)
time.sleep(2)
arduinoData.write(i.encode("ASCII"))
time.sleep(1.25)
arduinoData.write(str(calisma_modu).encode("ASCII"))
sure=[]
sicaklik=[]
basinc=[]
while 1:
        while arduinoData.in_waiting==0:
            pass
        arduinostring=arduinoData.readline()
        arduinolist=str(arduinostring).split(',')
        p=float(arduinolist[0].replace("b'",""))
        t=float(arduinolist[1])
        s=float(arduinolist[2].replace("\\r\\n'",""))
        sure.append(s)
        sicaklik.append(t)
        basinc.append(p)
        drawnow(makefig)
        #print("Sıcaklık: " + str(t)+", Basınç: "+str(p),end="\r")
        if len(sure)>16:
            sure.pop(0)
            sicaklik.pop(0)
            basinc.pop(0)