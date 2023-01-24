import os
from PIL import Image


carpeta_imagenes = 'C:/Users/jarim/OneDrive/Imágenes'

lista = []

for file in os.listdir(carpeta_imagenes):
    name, extension = os.path.splitext(file)
    if extension in [".jpg", "jpeg", ".png"]:
        imagen = Image.open(carpeta_imagenes+"/"+file)
        imagen = imagen.convert('RGB')

        lista.append(imagen)

if not lista:
   print("No se encontraron imágenes en la carpeta especificada o no tienen la extensión correcta.")
else:
    imagen_1 = lista[0]
    lista.pop(0)
    imagen_1.save(r'C:/Users/jarim/OneDrive/Imágenes/PDF/my_pdf.pdf',save_all=True,append_images=lista)
