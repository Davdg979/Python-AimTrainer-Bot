import pyautogui
import keyboard
import win32api
import win32con
import time

#Tela: 1600x900
#REGIÃO: 393, 232, 794, 477
#RGB: 255, 87, 34

r, g, b = 255, 87, 34

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

print("Pressione a tecla 'Z' para parar o bot...\n")

while keyboard.is_pressed("z") == False:
    im1 = pyautogui.screenshot(region=(393, 232, 794, 477))
    width, height = im1.size

    for x in range(0, width, 13):
        achou = 0
        for y in range(0, height, 13):
            r,g,b = im1.getpixel((x, y))

            if r == 255 and g == 87 and b == 34:
                achou = 1
                click(393+x, 232+y)
                time.sleep(0.05)
                break
            
        if achou == 1:
            break