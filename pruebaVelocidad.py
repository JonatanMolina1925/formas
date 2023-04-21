import pywt
import numpy as np
#import matplotlib.pyplot as plt
import time
#from scipy import signal
import math
#Variables para el calculo de caracteristicas
avgA = 0.0
avgd1 = 0.0
avgd2 = 0.0
avgd3 = 0.0
avgd4 = 0.0
enA = 0.0
end1 = 0.0
end2 = 0.0
end3 = 0.0
end4 = 0.0
rmsA = 0.0
rmsd1 = 0.0
rmsd2 = 0.0
rmsd3 = 0.0
rmsd4 = 0.0
desEstA = 0.0
desEstd1 = 0.0
desEstd2 = 0.0
desEstd3 = 0.0
desEstd4 = 0.0
skA = 0.0
skd1 = 0.0
skd2 = 0.0
skd3 = 0.0
skd4 = 0.0
krA = 0.0
krd1 = 0.0
krd2 = 0.0
krd3 = 0.0
krd4 = 0.0
frecuencia='9600'
perturbacion='interrupcion.csv'

#señal senoidal 
x = np.loadtxt(frecuencia+'/SinRuido/'+perturbacion, delimiter=',')
x10db = np.loadtxt(frecuencia+'/ConRuido/10db/'+perturbacion, delimiter=',')
x20db = np.loadtxt(frecuencia+'/ConRuido/20db/'+perturbacion, delimiter=',')
x30db = np.loadtxt(frecuencia+'/ConRuido/30db/'+perturbacion, delimiter=',')
print("Prueba de" +perturbacion+ " a "+frecuencia+" kHz\n")

inicio=time.time()
#Calculo de transformada
cA,CD1,CD2,CD3,CD4 = pywt.wavedec(x, 'db3', level=4)

#Calculo de promedio y rms
for n in cA:
    avgA=avgA+n
    rmsA=rmsA+math.pow(n,2)
    enA=enA+math.pow(n,2)
for n in CD1:
    avgd1=avgd1+n
    rmsd1=rmsd1+math.pow(n,2)
    end1=end1+math.pow(n,2)
for n in CD2:
    avgd2=avgd2+n
    rmsd2=rmsd2+math.pow(n,2)
    end2=end2+math.pow(n,2)
for n in CD3:
    avgd3=avgd3+n
    rmsd3=rmsd3+math.pow(n,2)
    end3=end3+math.pow(n,2)
for n in CD4:
    avgd4=avgd4+n
    rmsd4=rmsd4+math.pow(n,2)
    end4=end4+math.pow(n,2)

avgA=avgA/len(cA)
avgd1=avgd1/len(CD1)
avgd2=avgd2/len(CD2)
avgd3=avgd3/len(CD3)
avgd4=avgd4/len(CD4)

rmsA=math.sqrt(rmsA/len(cA))
rmsd1=math.sqrt(rmsA/len(CD1))
rmsd2=math.sqrt(rmsA/len(CD2))
rmsd3=math.sqrt(rmsA/len(CD3))
rmsd4=math.sqrt(rmsA/len(CD4))

for n in cA:
    desEstA=desEstA+math.pow(n-avgA,2)
for n in CD1:
    desEstd1=desEstd1+math.pow(n-avgd1,2)
for n in CD2:
    desEstd2=desEstd2+math.pow(n-avgd2,2)
for n in CD3:
    desEstd3=desEstd3+math.pow(n-avgd3,2)
for n in CD4:
    desEstd4=desEstd4+math.pow(n-avgd4,2)

desEstA=math.sqrt(desEstA/len(cA))
desEstd1=math.sqrt(desEstd1/len(CD1))
desEstd2=math.sqrt(desEstd2/len(CD2))
desEstd3=math.sqrt(desEstd3/len(CD3))
desEstd4=math.sqrt(desEstd4/len(CD4))

for n in cA:
    skA=skA+math.pow(n-avgA/desEstA,3)
    krA=krA+math.pow(n-avgA/desEstA,4)
for n in CD1:
    skd1=skd1+math.pow(n-avgd1/desEstd1,3)
    krd1=krd1+math.pow(n-avgd1/desEstd1,4)
for n in CD2:
    skd2=skd2+math.pow(n-avgd2/desEstd2,3)
    krd2=krd2+math.pow(n-avgd2/desEstd2,4)
for n in CD3:
    skd3=skd3+math.pow(n-avgd3/desEstd3,3)
    krd3=krd3+math.pow(n-avgd3/desEstd3,4)
for n in CD4:
    skd4=skd4+math.pow(n-avgd4/desEstd4,3)
    krd4=krd4+math.pow(n-avgd4/desEstd4,4)

skA=skA/len(cA)
skd1=skd1/len(CD1)
skd2=skd2/len(CD2)
skd3=skd3/len(CD3)
skd4=skd4/len(CD4)

krA=krA/len(cA)
krd1=krd1/len(CD1)
krd2=krd2/len(CD2)
krd3=krd3/len(CD3)
krd4=krd4/len(CD4)
fin=time.time()
print(str(fin-inicio)+" segundos, sin ruido\n")

############################ Ruido de 10 DB ########################################
avgA = 0.0
avgd1 = 0.0
avgd2 = 0.0
avgd3 = 0.0
avgd4 = 0.0
enA = 0.0
end1 = 0.0
end2 = 0.0
end3 = 0.0
end4 = 0.0
rmsA = 0.0
rmsd1 = 0.0
rmsd2 = 0.0
rmsd3 = 0.0
rmsd4 = 0.0
desEstA = 0.0
desEstd1 = 0.0
desEstd2 = 0.0
desEstd3 = 0.0
desEstd4 = 0.0
skA = 0.0
skd1 = 0.0
skd2 = 0.0
skd3 = 0.0
skd4 = 0.0
krA = 0.0
krd1 = 0.0
krd2 = 0.0
krd3 = 0.0
krd4 = 0.0
inicio=time.time()
#Calculo de transformada
cA10,CD110,CD210,CD310,CD410 = pywt.wavedec(x10db, 'db3', level=4)

#Calculo de promedio y rms
for n in cA10:
    avgA=avgA+n
    rmsA=rmsA+math.pow(n,2)
    enA=enA+math.pow(n,2)
for n in CD110:
    avgd1=avgd1+n
    rmsd1=rmsd1+math.pow(n,2)
    end1=end1+math.pow(n,2)
for n in CD210:
    avgd2=avgd2+n
    rmsd2=rmsd2+math.pow(n,2)
    end2=end2+math.pow(n,2)
for n in CD310:
    avgd3=avgd3+n
    rmsd3=rmsd3+math.pow(n,2)
    end3=end3+math.pow(n,2)
for n in CD410:
    avgd4=avgd4+n
    rmsd4=rmsd4+math.pow(n,2)
    end4=end4+math.pow(n,2)

avgA=avgA/len(cA10)
avgd1=avgd1/len(CD110)
avgd2=avgd2/len(CD210)
avgd3=avgd3/len(CD310)
avgd4=avgd4/len(CD410)

rmsA=math.sqrt(rmsA/len(cA10))
rmsd1=math.sqrt(rmsA/len(CD110))
rmsd2=math.sqrt(rmsA/len(CD210))
rmsd3=math.sqrt(rmsA/len(CD310))
rmsd4=math.sqrt(rmsA/len(CD410))

for n in cA10:
    desEstA=desEstA+math.pow(n-avgA,2)
for n in CD110:
    desEstd1=desEstd1+math.pow(n-avgd1,2)
for n in CD210:
    desEstd2=desEstd2+math.pow(n-avgd2,2)
for n in CD310:
    desEstd3=desEstd3+math.pow(n-avgd3,2)
for n in CD410:
    desEstd4=desEstd4+math.pow(n-avgd4,2)

desEstA=math.sqrt(desEstA/len(cA10))
desEstd1=math.sqrt(desEstd1/len(CD110))
desEstd2=math.sqrt(desEstd2/len(CD210))
desEstd3=math.sqrt(desEstd3/len(CD310))
desEstd4=math.sqrt(desEstd4/len(CD410))

for n in cA10:
    skA=skA+math.pow(n-avgA/desEstA,3)
    krA=krA+math.pow(n-avgA/desEstA,4)
for n in CD110:
    skd1=skd1+math.pow(n-avgd1/desEstd1,3)
    krd1=krd1+math.pow(n-avgd1/desEstd1,4)
for n in CD210:
    skd2=skd2+math.pow(n-avgd2/desEstd2,3)
    krd2=krd2+math.pow(n-avgd2/desEstd2,4)
for n in CD310:
    skd3=skd3+math.pow(n-avgd3/desEstd3,3)
    krd3=krd3+math.pow(n-avgd3/desEstd3,4)
for n in CD410:
    skd4=skd4+math.pow(n-avgd4/desEstd4,3)
    krd4=krd4+math.pow(n-avgd4/desEstd4,4)

skA=skA/len(cA10)
skd1=skd1/len(CD110)
skd2=skd2/len(CD210)
skd3=skd3/len(CD310)
skd4=skd4/len(CD410)

krA=krA/len(cA10)
krd1=krd1/len(CD110)
krd2=krd2/len(CD210)
krd3=krd3/len(CD310)
krd4=krd4/len(CD410)
fin=time.time()
print(str(fin-inicio)+" segundos, ruido 10DB\n")


############################ Ruido de 20 DB ########################################
avgA = 0.0
avgd1 = 0.0
avgd2 = 0.0
avgd3 = 0.0
avgd4 = 0.0
enA = 0.0
end1 = 0.0
end2 = 0.0
end3 = 0.0
end4 = 0.0
rmsA = 0.0
rmsd1 = 0.0
rmsd2 = 0.0
rmsd3 = 0.0
rmsd4 = 0.0
desEstA = 0.0
desEstd1 = 0.0
desEstd2 = 0.0
desEstd3 = 0.0
desEstd4 = 0.0
skA = 0.0
skd1 = 0.0
skd2 = 0.0
skd3 = 0.0
skd4 = 0.0
krA = 0.0
krd1 = 0.0
krd2 = 0.0
krd3 = 0.0
krd4 = 0.0
inicio=time.time()
#Calculo de transformada
cA20,CD120,CD220,CD320,CD420 = pywt.wavedec(x20db, 'db3', level=4)

#Calculo de promedio y rms
for n in cA20:
    avgA=avgA+n
    rmsA=rmsA+math.pow(n,2)
    enA=enA+math.pow(n,2)
for n in CD120:
    avgd1=avgd1+n
    rmsd1=rmsd1+math.pow(n,2)
    end1=end1+math.pow(n,2)
for n in CD220:
    avgd2=avgd2+n
    rmsd2=rmsd2+math.pow(n,2)
    end2=end2+math.pow(n,2)
for n in CD320:
    avgd3=avgd3+n
    rmsd3=rmsd3+math.pow(n,2)
    end3=end3+math.pow(n,2)
for n in CD420:
    avgd4=avgd4+n
    rmsd4=rmsd4+math.pow(n,2)
    end4=end4+math.pow(n,2)

avgA=avgA/len(cA20)
avgd1=avgd1/len(CD120)
avgd2=avgd2/len(CD220)
avgd3=avgd3/len(CD320)
avgd4=avgd4/len(CD420)

rmsA=math.sqrt(rmsA/len(cA20))
rmsd1=math.sqrt(rmsA/len(CD120))
rmsd2=math.sqrt(rmsA/len(CD220))
rmsd3=math.sqrt(rmsA/len(CD320))
rmsd4=math.sqrt(rmsA/len(CD420))

for n in cA20:
    desEstA=desEstA+math.pow(n-avgA,2)
for n in CD120:
    desEstd1=desEstd1+math.pow(n-avgd1,2)
for n in CD220:
    desEstd2=desEstd2+math.pow(n-avgd2,2)
for n in CD320:
    desEstd3=desEstd3+math.pow(n-avgd3,2)
for n in CD420:
    desEstd4=desEstd4+math.pow(n-avgd4,2)

desEstA=math.sqrt(desEstA/len(cA20))
desEstd1=math.sqrt(desEstd1/len(CD120))
desEstd2=math.sqrt(desEstd2/len(CD220))
desEstd3=math.sqrt(desEstd3/len(CD320))
desEstd4=math.sqrt(desEstd4/len(CD420))

for n in cA20:
    skA=skA+math.pow(n-avgA/desEstA,3)
    krA=krA+math.pow(n-avgA/desEstA,4)
for n in CD120:
    skd1=skd1+math.pow(n-avgd1/desEstd1,3)
    krd1=krd1+math.pow(n-avgd1/desEstd1,4)
for n in CD220:
    skd2=skd2+math.pow(n-avgd2/desEstd2,3)
    krd2=krd2+math.pow(n-avgd2/desEstd2,4)
for n in CD320:
    skd3=skd3+math.pow(n-avgd3/desEstd3,3)
    krd3=krd3+math.pow(n-avgd3/desEstd3,4)
for n in CD420:
    skd4=skd4+math.pow(n-avgd4/desEstd4,3)
    krd4=krd4+math.pow(n-avgd4/desEstd4,4)

skA=skA/len(cA20)
skd1=skd1/len(CD120)
skd2=skd2/len(CD220)
skd3=skd3/len(CD320)
skd4=skd4/len(CD420)

krA=krA/len(cA20)
krd1=krd1/len(CD120)
krd2=krd2/len(CD220)
krd3=krd3/len(CD320)
krd4=krd4/len(CD420)
fin=time.time()
print(str(fin-inicio)+" segundos, ruido 20DB\n")

############################ Ruido de 30 DB ########################################
avgA = 0.0
avgd1 = 0.0
avgd2 = 0.0
avgd3 = 0.0
avgd4 = 0.0
enA = 0.0
end1 = 0.0
end2 = 0.0
end3 = 0.0
end4 = 0.0
rmsA = 0.0
rmsd1 = 0.0
rmsd2 = 0.0
rmsd3 = 0.0
rmsd4 = 0.0
desEstA = 0.0
desEstd1 = 0.0
desEstd2 = 0.0
desEstd3 = 0.0
desEstd4 = 0.0
skA = 0.0
skd1 = 0.0
skd2 = 0.0
skd3 = 0.0
skd4 = 0.0
krA = 0.0
krd1 = 0.0
krd2 = 0.0
krd3 = 0.0
krd4 = 0.0
inicio=time.time()
#Calculo de transformada
cA30,CD130,CD230,CD330,CD430 = pywt.wavedec(x30db, 'db3', level=4)

#Calculo de promedio y rms
for n in cA30:
    avgA=avgA+n
    rmsA=rmsA+math.pow(n,2)
    enA=enA+math.pow(n,2)
for n in CD130:
    avgd1=avgd1+n
    rmsd1=rmsd1+math.pow(n,2)
    end1=end1+math.pow(n,2)
for n in CD230:
    avgd2=avgd2+n
    rmsd2=rmsd2+math.pow(n,2)
    end2=end2+math.pow(n,2)
for n in CD330:
    avgd3=avgd3+n
    rmsd3=rmsd3+math.pow(n,2)
    end3=end3+math.pow(n,2)
for n in CD430:
    avgd4=avgd4+n
    rmsd4=rmsd4+math.pow(n,2)
    end4=end4+math.pow(n,2)

avgA=avgA/len(cA30)
avgd1=avgd1/len(CD130)
avgd2=avgd2/len(CD230)
avgd3=avgd3/len(CD330)
avgd4=avgd4/len(CD430)

rmsA=math.sqrt(rmsA/len(cA30))
rmsd1=math.sqrt(rmsA/len(CD130))
rmsd2=math.sqrt(rmsA/len(CD230))
rmsd3=math.sqrt(rmsA/len(CD330))
rmsd4=math.sqrt(rmsA/len(CD430))

for n in cA30:
    desEstA=desEstA+math.pow(n-avgA,2)
for n in CD130:
    desEstd1=desEstd1+math.pow(n-avgd1,2)
for n in CD230:
    desEstd2=desEstd2+math.pow(n-avgd2,2)
for n in CD330:
    desEstd3=desEstd3+math.pow(n-avgd3,2)
for n in CD430:
    desEstd4=desEstd4+math.pow(n-avgd4,2)

desEstA=math.sqrt(desEstA/len(cA30))
desEstd1=math.sqrt(desEstd1/len(CD130))
desEstd2=math.sqrt(desEstd2/len(CD230))
desEstd3=math.sqrt(desEstd3/len(CD330))
desEstd4=math.sqrt(desEstd4/len(CD430))

for n in cA30:
    skA=skA+math.pow(n-avgA/desEstA,3)
    krA=krA+math.pow(n-avgA/desEstA,4)
for n in CD130:
    skd1=skd1+math.pow(n-avgd1/desEstd1,3)
    krd1=krd1+math.pow(n-avgd1/desEstd1,4)
for n in CD230:
    skd2=skd2+math.pow(n-avgd2/desEstd2,3)
    krd2=krd2+math.pow(n-avgd2/desEstd2,4)
for n in CD330:
    skd3=skd3+math.pow(n-avgd3/desEstd3,3)
    krd3=krd3+math.pow(n-avgd3/desEstd3,4)
for n in CD430:
    skd4=skd4+math.pow(n-avgd4/desEstd4,3)
    krd4=krd4+math.pow(n-avgd4/desEstd4,4)

skA=skA/len(cA30)
skd1=skd1/len(CD130)
skd2=skd2/len(CD230)
skd3=skd3/len(CD330)
skd4=skd4/len(CD430)

krA=krA/len(cA30)
krd1=krd1/len(CD130)
krd2=krd2/len(CD230)
krd3=krd3/len(CD330)
krd4=krd4/len(CD430)
fin=time.time()
print(str(fin-inicio)+" segundos, ruido 30DB\n")


#print("El promedio de cA es: "+str(avgA)+"\n")
#print("El promedio de CD1 es: "+str(avgd1)+"\n")
#print("El promedio de CD2 es: "+str(avgd2)+"\n")
#print("El promedio de CD3 es: "+str(avgd3)+"\n")
#print("El promedio de CD4 es: "+str(avgd4)+"\n")

#print("El rms de cA es: "+str(rmsA)+"\n")
#print("El rms de CD1 es: "+str(rmsd1)+"\n")
#print("El rms de CD2 es: "+str(rmsd2)+"\n")
#print("El rms de CD3 es: "+str(rmsd3)+"\n")
#print("El rms de CD4 es: "+str(rmsd4)+"\n")

#print("El energia de cA es: "+str(enA)+"\n")
#print("El energia de CD1 es: "+str(end1)+"\n")
#print("El energia de CD2 es: "+str(end2)+"\n")
#print("El energia de CD3 es: "+str(end3)+"\n")
#print("El energia de CD4 es: "+str(end4)+"\n")

#print("El Skewness de cA es: "+str(skA)+"\n")
#print("El Skewness de CD1 es: "+str(skd1)+"\n")
#print("El Skewness de CD2 es: "+str(skd2)+"\n")
#print("El Skewness de CD3 es: "+str(skd3)+"\n")
#print("El Skewness de CD4 es: "+str(skd4)+"\n")

#print("El Kurtosis de cA es: "+str(krA)+"\n")
#print("El Kurtosis de CD1 es: "+str(krd1)+"\n")
#print("El Kurtosis de CD2 es: "+str(krd2)+"\n")
#print("El Kurtosis de CD3 es: "+str(krd3)+"\n")
#print("El Kurtosis de CD4 es: "+str(krd4)+"\n")

#print("La desviacion estandar de cA es: "+str(desEstA)+"\n")
#print("La desciacion estandar de CD1 es: "+str(desEstd1)+"\n")
#print("La desviacion estandar de CD2 es: "+str(desEstd2)+"\n")
#print("La desviacion estandar de CD3 es: "+str(desEstd3)+"\n")
#print("La desviacion estandar de CD4 es: "+str(desEstd4)+"\n")

# plt.subplot(6,4,1), plt.plot(x)
# plt.title("Flicker sin ruido")
# plt.subplot(6,4,2), plt.plot(x10db)
# plt.title("Flicker con ruido 10DB")
# plt.subplot(6,4,3), plt.plot(x20db)
# plt.title("Flicker con ruido 20DB")
# plt.subplot(6,4,4), plt.plot(x30db)
# plt.title("Flicker con ruido 30DB")
# plt.subplot(6,4,5), plt.plot(cA)
# plt.subplot(6,4,6), plt.plot(cA10)
# plt.subplot(6,4,7), plt.plot(cA20)
# plt.subplot(6,4,8), plt.plot(cA30)
# plt.subplot(6,4,9), plt.plot(CD1)
# plt.subplot(6,4,10), plt.plot(CD110)
# plt.subplot(6,4,11), plt.plot(CD120)
# plt.subplot(6,4,12), plt.plot(CD130)
# plt.subplot(6,4,13), plt.plot(CD2)
# plt.subplot(6,4,14), plt.plot(CD210)
# plt.subplot(6,4,15), plt.plot(CD220)
# plt.subplot(6,4,16), plt.plot(CD230)
# plt.subplot(6,4,17), plt.plot(CD3)
# plt.subplot(6,4,18), plt.plot(CD310)
# plt.subplot(6,4,19), plt.plot(CD320)
# plt.subplot(6,4,20), plt.plot(CD330)
# plt.subplot(6,4,21), plt.plot(CD4)
# plt.subplot(6,4,22), plt.plot(CD410)
# plt.subplot(6,4,23), plt.plot(CD420)
# plt.subplot(6,4,24), plt.plot(CD430)
# # plt.subplot(7,1,8), plt.plot(CD4)
# plt.tight_layout()
# plt.show()
