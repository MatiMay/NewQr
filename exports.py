import tkinter as tk
from PIL import Image, ImageTk
import numpy as np


def mostrar_img(ruta_imagen, escala=1, pad_x=20, pad_y=20):
    ventana = tk.Tk()
    ventana.title("Visor de Imágenes")
    ventana.resizable(False, False)
    try:
        imagen_original = Image.open(ruta_imagen)

        etiqueta_imagen = tk.Label(ventana)
        etiqueta_imagen.pack(padx=pad_x, pady=pad_y)

        # escala: float >0 o int. resample por defecto Image.NEAREST (útil para estampa QR)
        def _show(escala_local=1, resample=Image.NEAREST):
            img = imagen_original
            if escala_local != 1:
                w, h = img.size
                new_size = (max(1, int(w * escala_local)), max(1, int(h * escala_local)))
                img = img.resize(new_size, resample=resample)

            imagen_tk = ImageTk.PhotoImage(img)
            # Reemplazar imagen en la etiqueta existente para que no se acumulen widgets
            etiqueta_imagen.configure(image=imagen_tk)
            etiqueta_imagen.image = imagen_tk

            # Ajustar tamaño de la ventana al contenido + padding para evitar recortes
            try:
                desired_w = img.size[0] + 2 * pad_x
                desired_h = img.size[1] + 2 * pad_y
                ventana.geometry(f"{desired_w}x{desired_h}")
            except Exception:
                pass
            ventana.update_idletasks()

        _show(escala)

        ventana._show_image_with_scale = _show

    except FileNotFoundError:
        etiqueta_error = tk.Label(ventana, text="Error: No se encontró la imagen.", fg="red")
        etiqueta_error.pack(padx=50, pady=50)
    
    ventana.mainloop()

def crear_img(matriz_rgb):
    if matriz_rgb is None:
        print("Error: La matriz de píxeles no puede ser None.")
        return

    arreglo_pixeles = np.array(matriz_rgb, dtype=np.uint8)

    imagen = Image.fromarray(arreglo_pixeles, 'RGB')

    imagen.save("mi_imagen_generada.png")
    
    return "mi_imagen_generada.png"