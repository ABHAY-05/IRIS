import speech_recognition as sr

def letter(my_name):
	listener = sr.Recognizer()
	with sr.Microphone() as source:
		print('Iris: Listening...')
		listener.pause_threshold=1
		listener.adjust_for_ambient_noise(source)
		voice = listener.listen(source)
	try:
		print('Iris: Recognising...')
		let = listener.recognize_google(voice, language="hi")
		if 'Iris' in let:
			let=let.replace('Iris','')
			let=let.lower()
			print(f'{my_name()}:{let}\n')
		else:
			print(f'{my_name()}: {let}\n')
	except Exception as e:
		print(f'{e}\n')
		return "n"
	return let