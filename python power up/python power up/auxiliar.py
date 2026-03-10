import time
import pyautogui

time.sleep(5) # tempo para o usuário posicionar o mouse onde deseja
print(pyautogui.position()) # mostra a posição do mouse (coordenadas x e y)