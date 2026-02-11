import json
import os
from datetime import datetime

# 1. Pedir los datos del nuevo empleo
print("🚀 NUEVA OFERTA LABORAL")
titulo = input("Puesto (ej. Cajero): ")
ubicacion = input("Ubicación (ej. Luque): ")
descripcion = input("Descripción corta: ")
link = input("Link de contacto (WhatsApp o Email): ")

# Fecha de hoy automática
fecha_hoy = datetime.today().strftime('%d/%m/%Y')

# Crear el diccionario del nuevo empleo
nuevo_empleo = {
    "titulo": titulo,
    "ubicacion": ubicacion,
    "fecha": fecha_hoy,
    "descripcion": descripcion,
    "link": link
}

# 2. Leer el archivo JSON actual
archivo = 'ofertas.json'

try:
    with open(archivo, 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    data = [] # Si no existe, creamos una lista vacía

# 3. Agregar el nuevo empleo AL PRINCIPIO de la lista (índice 0)
data.insert(0, nuevo_empleo)

# 4. Guardar el archivo JSON actualizado
with open(archivo, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✅ Archivo JSON actualizado correctamente.")

# 5. SUBIR A GITHUB AUTOMÁTICAMENTE
# Esto ejecuta comandos de terminal por ti
print("☁️ Subiendo a GitHub...")
os.system('git add ofertas.json')
os.system('git commit -m "Nueva oferta agregada desde script"')
os.system('git push origin main') # Ojo: si tu rama se llama 'master', cambia 'main' por 'master'

print("🎉 ¡LISTO! Tu página web se actualizará en 1 minuto.")