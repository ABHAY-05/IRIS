import os
import random
import sys
import webbrowser
import googletrans
import pyautogui
import pyjokes
import pyperclip
import pywhatkit
import speedtest
import wikipedia
from Modules.commands import speak, take_command, my_name, name_rem, name_know
from Modules.weather import weather
from Modules.News import news
from Modules.Email import email_info
from Modules.ChatBot import chatbot
from Modules.date_and_time import date_now, time_now
from Modules.wish import wish
from Modules.cpu import cpu
from Modules.g_search import google_search
from Modules.screenshot import screenshot
from Modules.pdf import read_pdf
from Modules.operations import Expression
from Modules.wikihow import wikihow
from Modules.letter import letter
from Modules.whatsapp import whatsapp
from Modules.record import recsound
from Modules.read import read
from Modules.keys import WEATHER, NEWS

translator = googletrans.Translator()

class IRIS:
	@staticmethod
	def Iris():
		wish(speak, my_name)
		while True:
			command=take_command()
			if all(word in command for word in ['play','youtube']) or all(word in command for word in ['search','youtube']):
				try:
					command=command.replace('play','').replace('iris','').replace('search','').replace('on','').replace('youtube','').strip()
					speak(f'playing {command}\n')
					pywhatkit.playonyt(command)
				except Exception as e:
					print(e)
					speak("sorry, some error has occurred")

			elif all(word in command for word in ['time','what']):
				time_now(speak)

			elif all(word in command for word in ['wikipedia','search']):
				try:
					command=command.replace('search','').replace('on','').replace('iris','').replace('wikipedia','').replace('for','').strip()
					info = wikipedia.summary(command, sentences=2)
					print('Iris: According to wikipedia')
					speak('According to wikipedia')
					print(f'Wikipedia: {info}\n')
					speak(info)
				except Exception as e:
					print(e)
					speak("sorry, some error has occurred")

			elif all(word in command for word in ['today','date']):
				date_now(speak)

			elif all(word in command for word in ['make','laugh']):
				joke=pyjokes.get_joke()
				print(f'Iris: {joke}\n')
				speak(joke)

			elif all(word in command for word in ['translate to']):
				try:
					command=command.replace("iris","")
					command=command.replace('translate to','')
					language=command.replace(" ","").strip()
					speak('what you want to translate?')
					command=take_command()
					translated = translator.translate(command, dest=language)
					translated = str(translated.text)
					print(translated)
					print('\n')
					speak(translated)
				except Exception as e:
					print(e)
					print('\n')
					speak("sorry, some error has occurred")

			elif all(word in command for word in ['search','chrome']):
				try:
					command=command.replace('search','').replace('on','').replace('iris','').replace('chrome','').replace('for','').strip()
					webbrowser.open(f"https://www.google.com/search?q={command}")
					print('Searching...\n')
					speak("searching your query on chrome")
				except Exception as e:
					print(e)
					print('\n')
					speak("sorry, some error has occurred")

			elif any(word in command for word in ['open chrome','open google']):
				speak("opening chrome")
				file=(open('files\\locations.txt','r').read()).splitlines()
				os.startfile(file[0])


			elif any(word in command for word in ['exit chrome','close chrome']):
				speak('closing chrome')
				os.system("TASKKILL /F /IM chrome.exe")

			elif all(word in command for word in ['google','search']):
				if('search on google' in command) or ('google search' in command):
					try:
						command=command.replace('search on google','').replace('iris','').replace('for','').replace('google search','').strip()
						google_search(command, speak)
					except Exception as e:
						print(e)
						print('\n')
						speak("sorry, some error has occurred")
				else:
					try:
						speak('what do you want to search on google?')
						search=take_command()
						google_search(search, speak)
					except Exception as e:
						print(e)
						print('\n')
						speak("sorry, some error has occurred")

			elif all(word in command for word in ['send','email']):
				try:
					email_info(command, speak, take_command, my_name)
				except Exception as e:
					print(f'{e}\n')
					speak("Unable to send the email")

			elif 'logout' in command:
				os.system("shutdown -l")

			elif 'shutdown' in command:
				os.system("shutdown /s /t 1")

			elif 'restart' in command:
				os.system("shutdown /r /t 1")

			elif all(word in command for word in ['write','note']):
				try:
					data=command.replace('write','').replace('a','').replace('iris','').replace('note','').replace('for','').replace('on','').strip()
					speak("you said me to note that"+data)
					remember = open('files\\data.txt','w')
					remember.write(data)
					remember.close()
				except Exception as e:
					print(e)
					print('\n')
					speak("sorry, some error has occurred")

			elif all(word in command for word in ['remember','anything']) or all(word in command for word in ['show','notes']):
				remember =open('files\\data.txt', 'r')
				speak(f"you said me to remember that {remember.read()}" )

			elif 'screenshot' in command:
				screenshot(speak, take_command, my_name)
				speak(f"Done {my_name()}!")

			elif 'cpu'in command:
				cpu(speak)

			elif any(word in command for word in ['sleep now','you can sleep','take a nap']):
				speak(f'okay {my_name()}, I am going to sleep you can call me anytime.')
				break

			elif any(word in command for word in ['what is my name','do you know me','tell me my name']):
				name_know()

			elif any(word in command for word in ['goodbye','bye','offline','quit','exit']):
				mes1=[f'Goodbye {my_name()}!, see you again',f'Bye {my_name()}!, thanks for giving your time',f'goodbye {my_name()}!, have a good day']
				res1=random.choice(mes1)
				speak(res1)
				sys.exit()

			elif 'open notepad' in command:
				speak('opening notepad')
				file=(open('files\\locations.txt','r').read()).splitlines()
				os.startfile(file[1])

			elif any(word in command for word in ['close notepad','exit notepad']):
				speak('closing notepad')
				os.system("TASKKILL /F /IM notepad.exe")

			elif all(word in command for word in ['read','pdf']):
				if 'read pdf file'in command:
					command=command.replace('read pdf file','').replace('iris','').replace('name','').replace('of','').replace('with','').replace('the','').replace(' ','').strip()
					read_pdf(command, speak, take_command)
				else:
					speak("tell me the name of pdf file")
					file_name=take_command()
					read_pdf(file_name, speak, take_command)

			elif any(word in command for word in ['change my name','update my name']):
				name_rem(command)

			elif all(word in command for word in ['you','robot']):
				mes8=['Yes I am a robot, but I’m a good one. Let me prove it. How can I help you?','Yes I’m a robot but I’m a smart one!']
				res3=random.choice(mes8)
				speak(res3)


			elif any(word in command for word in ['tell me something','tell me anything']):
				speak('do you want to hear a joke?')
				com=take_command()
				if 'yes' in com:
					joke=pyjokes.get_joke()
					print(f'Iris: {joke}\n')
					speak(joke)
				else:
					speak('So, what you want to do?')

			elif any(word in command for word in ['hi, my name is','my name is','hey, my name is','hello, my name is','my name is']):
				command=command.replace('my name is','')
				if 'hi' in command:
					command=command.replace('hi','').strip()
					speak(f'Hello, {command}, nice to meet you!')
				elif 'hey' in command:
					command=command.replace('hey','').strip()
					speak(f'Hello, {command}, nice to meet you!')
				elif 'hello' in command:
					command=command.replace('hello','').strip()
					speak(f'Hello, {command}, nice to meet you!')
				else:
					speak(f'hello, {command.strip()}, nice to meet you!')


			elif any(word in command for word in ['i have a question', 'can you help me']):
				mes5=['yes, i can help you. tell me what kind of problem you have','yes sure, tell me your problem']
				res6=random.choice(mes5)
				speak(res6)

			elif all(word in command for word in ['weather','report']) or all(word in command for word in ["weather","today"]):
				try:
					weather(command, WEATHER, speak, take_command)
				except Exception as e:
					print(e)

			elif any(word in command for word in ['what is your name','who are you']):
				mes6=['i am Iris, a voice assistant','my name is Iris, how can i help you']
				res7=random.choice(mes6)
				speak(res7)

			elif any(word in command for word in ['can you calculate','calculate','do some calculations']):
				try:
					if any(word in command for word in ['can you calculate','calculate']):
						comm=command.replace('can you calculate','').replace('iris','').replace('calculate','').strip()
						result=Expression(*(comm.split()))
						print(f'Iris: {result}\n')
						speak(result)
					else:
						speak("what you want to calculate")
						comm=take_command()
						result=Expression(*(comm.split()))
						print(f'Iris: {result}\n')
						speak(result)
				except Exception as e:
					print(f'{e}\n')
					speak('Wrong operand given')

			elif all(word in command for word in ['how to']):
				wikihow(command.replace('iris',''), speak)

			elif any(word in command for word in ['write a letter','write an application','write a diary']):
				try:
					command=command.replace('write','').replace('iris','').replace('letter','').replace('application','').replace('diary','').replace('a','').replace('of','').replace('on','').replace('for','').strip()
					speak('say what you want to write')
					let=letter(my_name)
					translated = translator.translate(let, dest='en')
					translated = str(translated.text)
					rem = open(f'files\\letter\\{command}.txt','w')
					rem.write(translated)
					rem.close()
				except Exception as e:
					print(e)
					speak("sorry, some error has occurred")

			elif all(word in command for word in ['read','letter']) or all(word in command for word in['read','application']) or all(word in command for word in['read','diary']):
				try:
					command=command.replace('read','').replace('iris','').replace('letter','').replace('application','').replace('diary','').replace('a','').replace('of','').replace('on','').replace(' ','').strip()
					re =open(f'files\\letter\\{command}.txt', 'r')
					print('Iris: Reading...')
					speak(f'Reading...  {re.read()}')
				except Exception as e:
					print(f'{e}\n')
					speak(f'could not find any file named {command}')

			elif 'volume up' in command:
				try:
					speak('how much times you want to increase the volume')
					up=int(take_command())
					pyautogui.press('volumeup',presses=up)
				except Exception as e:
					print(f'{e}\n')
				speak(f'done {my_name()}!')

			elif 'volume down' in command:
				try:
					speak('how much times you want to decrease the volume')
					down=int(take_command())
					pyautogui.press('volumedown',presses=down)
				except Exception as e:
					print(f'{e}\n')
					speak("sorry,  some error occurred")
				speak(f'done {my_name()}!')

			elif any(word in command for word in ['mute volume', 'unmute volume']):
				pyautogui.press('volumemute')
				print(f'done {my_name()}!')
				speak(f'done {my_name()}!')

			elif all(word in command for word in ['internet','speed']) or 'speed test' in command:
				try:
					speak('please wait i am testing speed')
					s = speedtest.Speedtest()
					s.get_best_server()
					s.download()
					s.upload()
					res = s.results.dict()
					dl=format(res["download"]/1000000,'0.2f')
					ul=format(res["upload"]/1000000,'0.2f')
					ping=format(res["ping"],'0.2f')
					print(f"Download: {dl} mbps\nUpload: {ul} mbps\nPing: {ping} ms\n")
					speak(f"Download speed: {dl} mega bits per second. Upload speed: {ul} mega bits per second. Ping: {ping}ms")
				except Exception as e:
					print(f'{e}\n')
					speak("sorry, some error has occurred")

			elif all(word in command for word in['open','epic games']):
				speak('opening Epic games launcher')
				file=(open('files\\locations.txt','r').read()).splitlines()
				os.startfile(file[2])

			elif any(word in command for word in ['close epic games','exit epic games']):
				speak('closing epic games launcher')
				os.system("TASKKILL /F /IM EpicGamesLauncher.exe")

			elif all(word in command for word in ['repeat','me']) or all(word in command for word in ['repeat','after me']):
				command=command.replace('repeat me','').replace('iris','').replace('after me','').strip()
				speak(command)

			elif all(word in command for word in ['today','news']):
				try:
					news(NEWS, speak, take_command, my_name)
				except Exception as e:
					print(f'{e}\n')
					speak('some error occurred')

			elif all(word in command for word in ['whatsapp','message']):
				try:
					if 'whatsapp message to' in command:
						command=command.replace('whatsapp','').replace('iris','').replace('message','').replace('to','').replace('send','').replace('a','').replace(' ','').strip()
						whatsapp(command, speak, take_command, my_name)
					else:
						speak("to whom you want to send the message")
						name=take_command()
						whatsapp(name, speak, take_command, my_name)
				except Exception as e:
					print(e)

			elif any(word in command for word in ['join zoom','launch zoom meeting','join zoom meeting']):
				try:
					speak('opening zoom')
					os.startfile("files\\zoom.bat")
				except Exception as e:
					print(f'{e}\n')

			elif any(word in command for word in ['close zoom','end zoom meeting','exit zoom']):
				speak('closing zoom')
				os.system('TASKKILL /F /IM cmd.exe')
				os.system('TASKKILL /F /IM zoom.exe')

			elif all(word in command for word in ['record','sound']):
				if ('record my' in command) or ('record me' in command):
					filename=command.replace('iris','').replace('record my','').replace('with','').replace('record me','').replace('sound','').replace('voice','').replace(' ','').strip()
					recsound(filename, speak, take_command)
				else:
					speak("what should i name the file of recording")
					filename=take_command()
					recsound(filename, speak, take_command)

			elif all(word in command for word in ['play','recording']) or all(word in command for word in ['play','sound']):
				try:
					filename=command.replace('play','').replace('recordings','').replace('iris','').replace('recording','').replace('sound','').replace('sounds','').replace('on','').replace('of','').replace(' ','').strip()
					os.startfile(f"files\\recordings\\{filename}.mp3")
				except Exception as e:
					print(f'{e}\n')
					speak('something went wrong')

			elif all(word in command for word in['close','music']) or all(word in command for word in['close','sound']) or all(word in command for word in['close','recording']):
				speak('closing sounds')
				os.system('TASKKILL /F /IM Music.UI.exe')

			elif all(word in command for word in ['text','type']):
				speak(f"okay i am listening,   speak{my_name()}")
				pyautogui.typewrite(take_command())

			elif all(word in command for word in ['select','all']):
				pyautogui.hotkey('ctrl','a')

			elif all(word in command for word in ['close','window']) or all(word in command for word in ['close','application']):
				pyautogui.hotkey('alt','f4')

			elif all(word in command for word in ['open','tab']):
				pyautogui.hotkey('ctrl','t')

			elif all(word in command for word in ['open','new window']):
				pyautogui.hotkey('ctrl','n')

			elif all(word in command for word in ['open','incognito']):
				pyautogui.hotkey('ctrl','shift','n')

			elif all(word in command for word in ['press','copy']):
				pyautogui.hotkey('ctrl','c')
				speak('text copied to clipboard')

			elif all(word in command for word in ['press','paste']):
				pyautogui.hotkey('ctrl','v')

			elif all(word in command for word in ['press','undo']):
				pyautogui.hotkey('ctrl','z')

			elif all(word in command for word in ['press','redo']):
				pyautogui.hotkey('ctrl','y')

			elif all(word in command for word in ['press','save']):
				pyautogui.hotkey('ctrl','s')

			elif all(word in command for word in ['press','back']):
				pyautogui.hotkey('browserback')

			elif all(word in command for word in ['press','page up']):
				pyautogui.hotkey('pageup')

			elif all(word in command for word in ['press','page down']):
				pyautogui.hotkey('pagedown')

			elif all(word in command for word in ['go to end','page']):
				pyautogui.hotkey('end')

			elif all(word in command for word in ['go to top','page']):
				pyautogui.hotkey('home')

			elif all(word in command for word in ['press','enter']):
				pyautogui.hotkey('enter')

			elif all(word in command for word in ['read','selected']):
				try:
					read(speak)
				except Exception as e:
					print(f'{e}\n')
					speak('something went wrong')

			elif all(word in command for word in['translate','selected']):
				try:
					language=command.replace("translate",'').replace('iris','').replace("selected","").replace("text","").replace("to","").replace(" ","").strip()
					pyautogui.hotkey("ctrl",'c')
					tobespoken=pyperclip.paste()
					content=tobespoken
					translated = translator.translate(content, dest=language)
					translated = str(translated.text)
					print(translated)
					print('\n')
					speak(translated)
				except Exception as e:
					print(e)
					print('\n')
					speak("sorry, some error has occurred")

			else:
				try:
					if len(command)>1:
						command=command.capitalize()
						command=command.replace('iris','')
						reply = chatbot().get_response(command)
						speak(reply)
				except Exception as e:
					print(f'{e}\n')

def main():
	while True:
		permission=take_command()
		if any(word in permission for word in ['iris','hello']):
			IRIS().Iris()
		elif any(word in permission for word in ['goodbye','bye','offline','quit','exit']):
			mes1=[f'Goodbye {my_name()}!, see you again',f'Bye {my_name()}!, thanks for giving your time',f'goodbye {my_name()}!, have a good day']
			res3=random.choice(mes1)
			speak(res3)
			sys.exit()

if __name__ == '__main__':
	main()