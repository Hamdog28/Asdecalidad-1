import numpy as np
import cv2
from cv2 import WINDOW_NORMAL
import itertools
import os

nombres_archivos=[]

for filename in os.listdir("files"):
    nombres_archivos.append(filename)    

archivos=[]
for nombre_archivo in nombres_archivos:
    
    img = cv2.imread("files/"+nombre_archivo)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    a=[]
    for i in gray:
        a=np.concatenate((a,i),axis=0)
    archivos.append(np.array(a)[:,None])
    

print(len(archivos))