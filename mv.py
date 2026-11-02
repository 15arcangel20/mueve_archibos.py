
import os
import shutil

# CARPETA DONDE BUSCAR LOS MP3
carpeta_origen = "/home/arcangel/Descargas/mp3"

# CARPETA DONDE REUNIR TODA LA MUSICA
carpeta_destino = "/home/arcangel/Descargas/musica"

# Crear carpeta de destino si no existe
os.makedirs(carpeta_destino, exist_ok=True)

contador = 0

# Recorrer todas las carpetas y subcarpetas
for raiz, carpetas, archivos in os.walk(carpeta_origen):

    for archivo in archivos:

        if archivo.lower().endswith(".mp3"):

            ruta_origen = os.path.join(raiz, archivo)
            ruta_destino = os.path.join(carpeta_destino, archivo)

            # Evitar sobrescribir archivos con el mismo nombre
            nombre, extension = os.path.splitext(archivo)
            numero = 1

            while os.path.exists(ruta_destino):
                nuevo_nombre = f"{nombre}_{numero}{extension}"
                ruta_destino = os.path.join(
                    carpeta_destino, nuevo_nombre
                )
                numero += 1

            # Mover archivo
            shutil.move(ruta_origen, ruta_destino)

            contador += 1
            print(f"Movido: {ruta_origen}")

print("\nProceso terminado.")
print(f"Total de MP3 movidos: {contador}")