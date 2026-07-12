import numpy as np
from exports import crear_img, mostrar_img

tamaño = 21 

estampa= np.zeros((7, 7, 3), dtype=np.uint8)

def valores_rgb(matriz):
    for i in range(tamaño):
        for j in range(tamaño):
            px= np.random.randint(0,4)
            if px==0:
                matriz[i,j]= [0,0,0]
            elif px==1:
                matriz[i,j]= [255,0,0]
            elif px==2:
                matriz[i,j]= [0,255,0]
            elif px==3:
                matriz[i,j]= [0,0,255]
            
    return matriz

matriz = np.full((tamaño, tamaño, 3), [255, 255, 255], dtype=np.uint8)

#
# cada pixel puede ser de 4 valores: 0=negro, 1=rojo, 2=verde, 3=azul
#


#print_matriz(matriz)
matriz = valores_rgb(matriz)
mostrar_img(crear_img(matriz), 10)