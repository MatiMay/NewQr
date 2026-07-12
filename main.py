import numpy as np
from exports import crear_img, mostrar_img

tamaño = 100 
divisores= [3, 5, 15]#17, 51, 85
x= divisores[0] #3
y= 255/x        #85

def print_matriz(matriz):
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            print(f"Pixel ({i}, {j}): {matriz[i, j]}")
    return

def valores_random(matriz):
    for i in range(tamaño):
        for j in range(tamaño):
            #matriz[i, j] = np.random.randint(0, 255, size=3)
            matriz[i,j]= np.random.randint(0, x, size=3)
            matriz[i,j]= matriz[i,j]*y
    return matriz

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

matriz_ejemplo = np.full((tamaño, tamaño, 3), [255, 255, 255], dtype=np.uint8)


#print_matriz(matriz_ejemplo)
matriz = valores_rgb(matriz_ejemplo)
mostrar_img(crear_img(matriz), 4)