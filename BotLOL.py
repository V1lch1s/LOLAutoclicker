#Bot de League of Legends (Explorador)
import threading
import subprocess

# Importar y ejecutar main_script en un subproceso
def run_main():
    subprocess.run(["python", "Clicker.py"])

# Importar y ejecutar AFKhandler_script en un subproceso
def run_afkhandler():
    subprocess.run(["python", "AFKhandler.py"])

# Crear dos subprocesos para ejecutar los scripts simultáneamente
main_thread = threading.Thread(target=run_main)
afkhandler_thread = threading.Thread(target=run_afkhandler)

# Iniciar los subprocesos
main_thread.start()
afkhandler_thread.start()

# Esperar a que todos los subprocesos terminen
main_thread.join()
afkhandler_thread.join()
