import time
import pyautogui

def screenshot(speak, take_command, my_name):
	speak(f'{my_name()} ,please tell me the name of this screenshot file')
	file_name=take_command().strip()
	speak('please hold the screen for few seconds, i am taking screenshot')
	time.sleep(1)
	img = pyautogui.screenshot()
	img.save(f"files\\screenshots\\{file_name}.png")