import time
import pyautogui

index = 0
tabs = 1

time.sleep(6)

def realizar_acciones():
    pyautogui.hotkey('ctrl', 'e')
    time.sleep(0.1)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)

    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)

    pyautogui.press('enter')
    time.sleep(0.1)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)

    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)

    pyautogui.hotkey('ctrl', 'w')
    time.sleep(0.1)

    global index
    index += 1
    
if __name__ == "__main__":
    try:
        while index < tabs:
            realizar_acciones()
    except KeyboardInterrupt:
        print("Error")
