# **LOL Autoclicker** 💀
---

#**Warning**

The program provided in this repository is outdated and it was not possible to update it after the end of 2023 due to new terms and conditions within the game that include the implementation of the famous and controversial Riot Vanguard anti-cheat that works as a driver at the kernel level, however, I don't have the time or need to update and recondition it to work with a DMA device or as a driver that bypasses Riot Vanguard. It is considered within the focus of cheating within the game and the distorted concept about what they (at their convenience) consider punishable. This application was developed in Python with an experimental and educational purpose and at no time was there any intention to use it as a means or as a trap within the game. I am not responsible for any misuse of this application and it should be used **AT YOUR OWN RISK**.
The consequences vary according to Riot's terms and conditions and include the banning of your account(s) and, in the most extreme case, your HWID (unique identifier for each device and is usually not alterable).


---
This is a League of Legends complex bot. Able to Spam Games again the AI again and again and doesn't stop until you keep pressed [ESC]

The first time you need to wait a few minutes in-game to generate cache for this bot and so that its execution can be easier and more fluid. It is very important to **previously execute in a controlled environment**

![Excecution Samp](https://github.com/V1lch1s/LOLAutoclicker/assets/143208742/3b9dc9b1-a4c6-4c7d-b4f2-5f2fcaef7714)

---

# Descripción
El desarrollo de este bot fue utilizando librerías de reconocimiento y automatización:
- keyboard
- pyautogui
- pygetwindow
- pywintypes
- time
- pywin32 (win32api and win32con)
- threading
- subprocess
---

# Scripts
## AFKhandler.py
```
from Clicks import *
from BuyItem import *
import keyboard

def AFKhandler():
    while keyboard.is_pressed("Esc") != True:
        try:
            # Manage AFK
            if pyautogui.locateOnScreen('AFK.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('AFK.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                keyboard.press('b')
                keyboard.release('b')
                time.sleep(10)
                BuyItem()
                time.sleep(1)

            if pyautogui.locateOnScreen('AFK2.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('AFK2.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                keyboard.press('b')
                keyboard.release('b')
                time.sleep(10)
                BuyItem()
                time.sleep(1)

            if pyautogui.locateOnScreen('AFK3.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('AFK3.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)

            if pyautogui.locateOnScreen('ProfessorQuit.jpg', confidence = 0.9) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('ProfessorQuit.jpg', confidence = 0.9)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)

            if pyautogui.locateOnScreen('LevelUp.jpg', confidence = 0.85) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('LevelUp.jpg', confidence = 0.85)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)

            if pyautogui.locateOnScreen('Fijar.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('Fijar.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                pyautogui.moveTo(center_x, center_y)
                leftClick(center_x, center_y)

            if pyautogui.locateOnScreen('EliseR.jpg', confidence = 0.8):
                keyboard.press('r')
                keyboard.release('r')

            # Reconectar
            if pyautogui.locateOnScreen('Reconectar.jpg', confidence = 0.75) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('Reconectar.jpg', confidence = 0.75)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)

            # Reconectar (Segundo botón)
            if pyautogui.locateOnScreen('Reconectar2.jpg', confidence = 0.75) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('Reconectar2.jpg', confidence = 0.75)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
        except TypeError or OSError or ValueError:
            pass

if __name__ == "__main__":
    
    AFKhandler()
```

This code is the responsible of not being detected by LeaveBuster as an AFK if the AFK window is spawned in the game.
---

## BuyItem.py
```
import keyboard
import pywintypes
from Clicks import *

def BuyItem():
    try:
        keyboard.press('t')  #Abre la tienda
        keyboard.release('t')

        for i in range(50):
            if pyautogui.locateOnScreen('item.jpg', confidence = 0.75) != None and pyautogui.locateOnScreen('Object_True.jpg', confidence = 0.75):
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('Object_True.jpg', confidence = 0.75)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                pyautogui.moveTo(center_x, center_y)
                leftClick(center_x, center_y)
                time.sleep(0.1)
                leftClick(center_x, center_y)
                time.sleep(0.1)
                leftClick(center_x, center_y)
                time.sleep(0.1)
                leftClick(center_x, center_y) #Compra el objeto
                break
            
            if pyautogui.locateOnScreen('item1.jpg', confidence = 0.75) != None and pyautogui.locateOnScreen('Object_True.jpg', confidence = 0.75):
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('Object_True.jpg', confidence = 0.75)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                pyautogui.moveTo(center_x, center_y)
                leftClick(center_x, center_y)
                time.sleep(0.1)
                leftClick(center_x, center_y)
                time.sleep(0.1)
                leftClick(center_x, center_y)
                time.sleep(0.1)
                leftClick(center_x, center_y) #Compra el objeto
                break
                
            if pyautogui.locateOnScreen('item2.jpg', confidence = 0.75) != None and pyautogui.locateOnScreen('Object_True.jpg', confidence = 0.75):
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('Object_True.jpg', confidence = 0.75)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                pyautogui.moveTo(center_x, center_y)
                leftClick(center_x, center_y)
                time.sleep(0.1)
                leftClick(center_x, center_y)
                time.sleep(0.1)
                leftClick(center_x, center_y)
                time.sleep(0.1)
                leftClick(center_x, center_y) #Compra el objeto
                break

            if keyboard.is_pressed("Esc") == True:
                break
            
        keyboard.press('t') #Cierra la tienda
        keyboard.release('t')

    except TypeError or OSError or ValueError:
        pass

if __name__ == "__main__":
    
    BuyItem()
```

This code pick an item from the store in specific moments inside the program execution, for example, before start the route.
---

## Clicker.py
```
#Bot de League of Legends (Explorador)
import keyboard
import pywintypes
import pygetwindow as gw
from AFKhandler import *
from BuyItem import *

def route():
    images = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png','16.png']
    time.sleep(16)
    keyboard.press('u')
    keyboard.release('u')
    BuyItem()
    time.sleep(1)
    
    while pyautogui.locateOnScreen('Map.jpg', confidence = 0.85) or pyautogui.locateOnScreen('Map2.jpg', confidence = 0.85) or pyautogui.locateOnScreen('Map3.jpg', confidence = 0.85) or pyautogui.locateOnScreen('Map4.jpg', confidence = 0.85) != None and keyboard.is_pressed("Esc") != True:
        for i in range(len(images)):

            if keyboard.is_pressed("Esc") == True:
                break
            
            result = pyautogui.locateOnScreen(images[i], confidence = 0.75)
            if pyautogui.locateOnScreen('Map.jpg', confidence = 0.85) or pyautogui.locateOnScreen('Map2.jpg', confidence = 0.85) or pyautogui.locateOnScreen('Map3.jpg', confidence = 0.85) or pyautogui.locateOnScreen('Map4.jpg', confidence = 0.85) != None:
                if result != None:
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = result
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    pyautogui.moveTo(center_x, center_y)
                    rightClick(center_x, center_y)
                    time.sleep(20)
            
            else:
                print('Fuera de partida.')
                break
            
def main():
    print('Iniciando . . .')
    while keyboard.is_pressed("Esc") != True:
        try:
            # Ventana del launcher siempre activa
            window_name = "League of Legends"

            # Obtén la ventana por su nombre
            window = gw.getWindowsWithTitle(window_name)

            # Verifica si se encontró una ventana con ese nombre
            if len(window) > 0:
                # Si se encontró, verifica si la ventana está inactiva
                if not window[0].isActive:
                    # Activa la ventana
                    window[0].activate()
                else:
                    pass
            else:
                pass
            
            # Buscar Partida
            if pyautogui.locateOnScreen('TeammateMode.jpg', confidence = 0.8) != None or pyautogui.locateOnScreen('EnCola.jpg', confidence = 0.8) != None:
                # Aceptar Partida
                while pyautogui.locateOnScreen('EnCola.jpg', confidence = 0.8) != None:
                    print('Esperando Partida . . .')
                    time.sleep(0.01)
                
                    if pyautogui.locateOnScreen('startBattle.jpg', confidence = 0.6) != None:
                        # Obtiene las coordenadas del centro de la imagen detectada
                        x, y, width, height = pyautogui.locateOnScreen('startBattle.jpg', confidence = 0.6)
                        center_x = x + width // 2
                        center_y = y + height // 2
                        
                        # Mueve el mouse al centro de la imagen detectada y realiza un clic
                        leftClick(center_x, center_y)
                        
                        # Agrega un retraso antes de buscar la imagen nuevamente
                        time.sleep(1)
            else:
                if pyautogui.locateOnScreen('Play.jpg', confidence = 0.7) != None or pyautogui.locateOnScreen('EnCola.jpg', confidence = 0.8) != None:
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('Play.jpg', confidence = 0.7)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)

                    # Aceptar Partida
                    while pyautogui.locateOnScreen('EnCola.jpg', confidence = 0.8) != None and keyboard.is_pressed("Esc") != True:
                        print('Esperando Partida . . .')
                        time.sleep(0.01)
                    
                    if pyautogui.locateOnScreen('startBattle.jpg', confidence = 0.6) != None:
                        # Obtiene las coordenadas del centro de la imagen detectada
                        x, y, width, height = pyautogui.locateOnScreen('startBattle.jpg', confidence = 0.6)
                        center_x = x + width // 2
                        center_y = y + height // 2
                        
                        # Mueve el mouse al centro de la imagen detectada y realiza un clic
                        leftClick(center_x, center_y)
                        
                        # Agrega un retraso antes de buscar la imagen nuevamente
                        time.sleep(1)
                        
                
                if pyautogui.locateOnScreen('Play2.jpg', confidence = 0.8) != None or pyautogui.locateOnScreen('EnCola.jpg', confidence = 0.8) != None:
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('Play2.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)

                    # Aceptar Partida
                    while pyautogui.locateOnScreen('EnCola.jpg', confidence = 0.8) != None and keyboard.is_pressed("Esc") != True:
                        print('Esperando Partida . . .')
                        time.sleep(0.01)
                    
                    if pyautogui.locateOnScreen('startBattle.jpg', confidence = 0.6) != None:
                        # Obtiene las coordenadas del centro de la imagen detectada
                        x, y, width, height = pyautogui.locateOnScreen('startBattle.jpg', confidence = 0.6)
                        center_x = x + width // 2
                        center_y = y + height // 2
                        
                        # Mueve el mouse al centro de la imagen detectada y realiza un clic
                        leftClick(center_x, center_y)
                        
                        # Agrega un retraso antes de buscar la imagen nuevamente
                        time.sleep(1)
                
            # Seleccionar Campeón
            if pyautogui.locateOnScreen('PickChoGath.jpg', confidence = 0.7) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('PickChoGath.jpg', confidence = 0.7)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                pyautogui.moveTo(center_x, center_y)
                leftClick(center_x, center_y)

            if pyautogui.locateOnScreen('PickBelVeth.jpg', confidence = 0.7) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('PickBelVeth.jpg', confidence = 0.7)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                pyautogui.moveTo(center_x, center_y)
                leftClick(center_x, center_y)

            if pyautogui.locateOnScreen('PickMundo.jpg', confidence = 0.7) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('PickMundo.jpg', confidence = 0.7)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                pyautogui.moveTo(center_x, center_y)
                leftClick(center_x, center_y)
                
            if pyautogui.locateOnScreen('PickElise.jpg', confidence = 0.7) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('PickElise.jpg', confidence = 0.7)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                pyautogui.moveTo(center_x, center_y)
                leftClick(center_x, center_y)

            if pyautogui.locateOnScreen('PickBrand.jpg', confidence = 0.7) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('PickBrand.jpg', confidence = 0.7)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                pyautogui.moveTo(center_x, center_y)
                leftClick(center_x, center_y)
                
            if pyautogui.locateOnScreen('PickAlistar.jpg', confidence = 0.7) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('PickAlistar.jpg', confidence = 0.7)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                pyautogui.moveTo(center_x, center_y)
                leftClick(center_x, center_y)

            
            if pyautogui.locateOnScreen('Map.jpg', confidence = 0.85) or pyautogui.locateOnScreen('Map2.jpg', confidence = 0.85) or pyautogui.locateOnScreen('Map3.jpg', confidence = 0.85) or pyautogui.locateOnScreen('Map4.jpg', confidence = 0.85) != None:
                print('Partida detectada . . .')
                route()

            if pyautogui.locateOnScreen('Omitir.jpg', confidence = 0.8) != None:
                print('Esperando Página de Honor . . .')

                # Ventana del launcher siempre activa
                window_name = "League of Legends"

                # Obtén la ventana por su nombre
                window = gw.getWindowsWithTitle(window_name)

                # Verifica si se encontró una ventana con ese nombre
                if len(window) > 0:
                    # Si se encontró, verifica si la ventana está inactiva
                    if not window[0].isActive:
                        # Activa la ventana
                        window[0].activate()
                    else:
                        pass
                else:
                    pass
                    
                while pyautogui.locateOnScreen('HonorPage.jpg', confidence = 0.9) == None and keyboard.is_pressed("Esc") != True:
                    time.sleep(0.01)

            if pyautogui.locateOnScreen('HonorPage.jpg', confidence = 0.9) != None:
                print('Página de Honor. . .')
                    
            while pyautogui.locateOnScreen('HonorPage.jpg', confidence = 0.9) != None and keyboard.is_pressed("Esc") != True:
                if pyautogui.locateOnScreen('HonorTryndamere.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorTryndamere.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break

                if pyautogui.locateOnScreen('HonorChoGath.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorChoGath.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break

                if pyautogui.locateOnScreen('HonorBelVeth.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorBelVeth.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break

                if pyautogui.locateOnScreen('HonorMundo.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorMundo.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break

                if pyautogui.locateOnScreen('HonorElise.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorElise.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break
                
                if pyautogui.locateOnScreen('HonorAatrox.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorAatrox.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break
                    
                if pyautogui.locateOnScreen('HonorIllaoi.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorIllaoi.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break

                if pyautogui.locateOnScreen('HonorViego.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorViego.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break

                if pyautogui.locateOnScreen('HonorYone.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorYone.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break
                    
                if pyautogui.locateOnScreen('HonorKayn.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorKayn.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break

                if pyautogui.locateOnScreen('HonorNasus.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorNasus.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2

                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break            

                if pyautogui.locateOnScreen('HonorMorde.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorMorde.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break
                
                if pyautogui.locateOnScreen('HonorTristana.jpg', confidence = 0.8) != None:
                    print('Honrando...')
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('HonorTristana.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Mueve el mouse al centro de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    leftClick(center_x, center_y)
                    break
            
            if pyautogui.locateOnScreen('Continuar2.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('Continuar2.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
            if pyautogui.locateOnScreen('Restart.jpg', confidence = 0.7) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('Restart.jpg', confidence = 0.7)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)

            if pyautogui.locateOnScreen('Restart2.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('Restart2.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)


        except TypeError or OSError:
            time.sleep(0.01)

if __name__ == "__main__":

    main()
```

This code was expected to be the Core Script, but over the development time it became more difficult to execute and understand, so I turned it into a subroutine, which in turn is the central routine of the program's operation.
---

## Clicks.py
```
import pyautogui
import time
import win32api, win32con #pywin32


def rightClick(x,y):
    try:
        if pyautogui.locateOnScreen('NorthMap.png', confidence = 0.3) != None or pyautogui.locateOnScreen('SouthMap.png', confidence = 0.3) != None:
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
            time.sleep(0.001) #This pauses the script for 0.001 seconds
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    except pywintypes.error:
        time.sleep(1)
    
def leftClick(x,y):
    try:
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.001)  # This pauses the script for 0.001 seconds
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    except pywintypes.error:
        time.sleep(1)
```

This is a small library with a couple of functions used around the whole program. Without a doubt one of the 2 most important scripts.
---

## DetectionTest.py
```
from Clicks import *
import pyautogui
import keyboard

while keyboard.is_pressed("Esc") != True:
        try:
                if pyautogui.locateOnScreen("./crab/1.jpg", confidence = 0.6):
                        print("Cangrejo detectado 1")

                if pyautogui.locateOnScreen("./crab/2.jpg", confidence = 0.6):
                        print("Cangrejo detectado 2")

                if pyautogui.locateOnScreen("./crab/3.jpg", confidence = 0.6):
                        print("Cangrejo detectado 3")

                if pyautogui.locateOnScreen("./crab/4.jpg", confidence = 0.6):
                        print("Cangrejo detectado 4")

                if pyautogui.locateOnScreen("./crab/5.jpg", confidence = 0.6):
                        print("Cangrejo detectado 5")

                if pyautogui.locateOnScreen("./crab/6.jpg", confidence = 0.6):
                        print("Cangrejo detectado 6")

                if pyautogui.locateOnScreen("./crab/7.jpg", confidence = 0.6):
                        print("Cangrejo detectado 7")
                
        except TypeError or OSError:
            pass
```

This is not part of the app's schematic, but was used to test the accuracy of detecting game elements in app development by running this script instead of the program.
---

## BotLOL.py
```
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
```

This is the main script of the app, it uses threading to divide the execution into parts of the program so that they can all be executed at the same time as subprocesses, thus following a layered execution scheme, where the lowest layer executes the autoclicker and in the highest one the program is executed that checks that everything is in order (AFKhandler.py).
---

## Nota.txt and PersistedSettings.json
I am not going to put them here, but it is important to review them when testing the application **(HIGHLY NOT RECOMMENDED)**, since they are the **Execution Conditions**, that is, what the program needs to work and the environment to which it was adapted and develops.

