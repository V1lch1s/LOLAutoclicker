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
