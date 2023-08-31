import pyautogui
import pyperclip

def read(speak):
    pyautogui.hotkey("ctrl",'c')
    tobespoken=pyperclip.paste()
    speak(tobespoken)