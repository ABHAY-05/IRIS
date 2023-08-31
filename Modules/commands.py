import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

def speak(voice):
	engine.say(voice)
	engine.runAndWait()

def take_command():
	listener = sr.Recognizer()
	try:
		with sr.Microphone() as source:
			print('Iris: Listening...')
			listener.pause_threshold=1
			listener.energy_threshold=2000
			listener.adjust_for_ambient_noise(source)
			voice = listener.listen(source, phrase_time_limit=6)
			print('Iris: Recognising...')
			command = listener.recognize_google(voice)
			command=command.lower()
			print(f'{my_name()}: {command}\n')
	except Exception as e:
		print(f'{e}\n')
		return "n"
	return command.lower()

def name_rem(name):
	try:
		if 'my name is' in name:
			name = name.replace('my name is',"").replace('iris','')
			name = name.replace(' ',"").strip()
			speak(f"you said your name is {name}")
			rem = open('files\\name.txt','w')
			rem.write(name)
			rem.close()
		elif ('update my name' in name) or 'change my name':
			name = name.replace('update my name',"").replace('change my name','').replace('iris','').replace('to','')
			name = name.replace(' ',"").strip()
			speak(f"you name is updated to {name}")
			rem = open('files\\name.txt','w')
			rem.write(name)
			rem.close()
		else:
			name=name.strip()
			speak(f"you said your name is {name}")
			rem = open('files\\name.txt','w')
			rem.write(name)
			rem.close()
	except Exception as e:
		print(e)
		print('\n')
		speak("sorry, some error occurred")

def name_know():
	rem =open('files\\name.txt', 'r')
	user=rem.read()
	if len(user)>0:
		mes4=[f'You told me that your name is {user}',f'how are you {user}']
		res4=random.choice(mes4)
		speak(res4)
	else:
		speak("i don't Know you name. You can tell me your name so I can remember.")
		speak('what is your name?')
		name=take_command()
		name_rem(name)

def my_name():
	rem = open('files\\name.txt', 'r')
	user=rem.read()
	return user.upper()
