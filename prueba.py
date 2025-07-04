import subprocess

ruta = r'C:\Program Files (x86)\MuseScore 2\bin\MuseScore.exe'

try:
    subprocess.run([ruta], check=True)
    print("MuseScore se abrió correctamente.")
except Exception as e:
    print("Error al abrir MuseScore:", e)
