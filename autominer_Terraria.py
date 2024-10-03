import keyboard
import pyautogui

def startMining():
    pyautogui.mouseDown()

def stopMining():
    pyautogui.mouseUp()

def on_key_event(e):
    global mining  # Declarar 'mining' como global

    if e.name == '`':  # Verifica si la tecla presionada es ` (backtick)
        if mining:
            print("stopping mining")
            mining = False
            stopMining()
        else:
            print("starting mining")
            mining = True
            startMining()

if __name__ == "__main__":
    mining = False
    keyboard.on_press(on_key_event)
    keyboard.wait('-')
