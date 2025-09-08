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
