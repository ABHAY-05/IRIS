import time
import webbrowser
import pyautogui
import os

def whatsapp(name, speak, take_command, my_name):
	webbrowser.open("https://web.whatsapp.com/")
	speak('tell me the message you want to sent')
	mes=take_command()
	time.sleep(10)
	position = pyautogui.locateOnScreen("files\\buttons\\search.png")
	pyautogui.moveTo(position)
	pyautogui.click()
	time.sleep(1)
	pyautogui.typewrite(name)
	time.sleep(1)
	pyautogui.press("enter")
	time.sleep(2)
	pyautogui.typewrite(mes)
	time.sleep(0)
	pyautogui.press('enter')
	time.sleep(3)
	os.system('TASKKILL /F /IM chrome.exe')
	speak(f'done {my_name()}')