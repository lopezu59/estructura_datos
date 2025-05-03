import os
import cv2
import numpy as np


input_folder = 'imagenes_proyect/imagenes_originales'      # Carpeta con imágenes originales
output_folder = 'imagenes_proyect/imagenes_sin_marcas'     # Carpeta para guardar resultados
watermark_area = (280, 300, 740, 520)     # (x1, y1, x2, y2): zona de la marca

os.makedirs(output_folder, exist_ok=True)

# Procesar cada imagen en la carpeta
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, filename)
        img = cv2.imread(image_path)

        if img is None:
            print(f"No se pudo cargar {filename}")
            continue

        # Copia la zona alrededor de la marca para rellenar (efecto parche)
        x1, y1, x2, y2 = watermark_area
        patch = img[y1-10:y1, x1:x2]  # Zona justo arriba de la marca
        for y in range(y1, y2):
            img[y, x1:x2] = patch[0]

        # Guardar imagen sin marca
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, img)
        print(f"Procesado: {filename}")

print("✅ Proceso completo.")