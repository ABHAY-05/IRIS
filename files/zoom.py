import keyboard, time, subprocess
import pandas as pd
from datetime import datetime
import pyautogui

hashes = "#" * 95

print('\n', hashes)

print('\nYou can exit this program using ( Ctrl+c ) at any time')

print('\n', hashes)

df = pd.read_csv('meetingschedule.csv')
df_new = pd.DataFrame()
while True:
    timestr = datetime.now().strftime("%H:%M")

    if timestr in df.Time.values:
        df_new = df[df['Time'].astype(str).str.contains(timestr)]

        file = (open('files\\locations.txt', 'r').read()).splitlines()
        subprocess.Popen(file[3])
        time.sleep(6)

        pyautogui.mouseUp(button='left', x=763, y=420)
        pyautogui.click()
        time.sleep(2)

        keyboard.write(df_new.iloc[0, 1])

        position = pyautogui.locateOnScreen("files\\buttons\\turn_off_vid_button.png")
        pyautogui.moveTo(position)
        pyautogui.click()
        time.sleep(2)

        position = pyautogui.locateOnScreen("files\\buttons\\join_button_2.png")
        pyautogui.moveTo(position)
        pyautogui.click()
        time.sleep(4)

        keyboard.write(str(df_new.iloc[0, 2]))
        time.sleep(3)

        position = pyautogui.locateOnScreen("files\\buttons\\join_meeting.png")
        pyautogui.moveTo(position)
        pyautogui.click()

        time.sleep(60)

