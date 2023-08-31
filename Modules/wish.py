import datetime

def wish(speak, my_name):
	hour=int(datetime.datetime.now().hour)
	if 0 <= hour < 12:
		speak(f'good morning {my_name()}')

	elif 12 <= hour < 18:
		speak(f'good afternoon {my_name()}')

	else:
		speak(f'good evening {my_name()}')
	speak("I am Iris, how can i help you.")