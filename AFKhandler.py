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
