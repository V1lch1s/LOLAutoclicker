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
