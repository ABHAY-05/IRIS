import datetime

def time_now(speak):
	Time = datetime.datetime.now().strftime('%I:%M %p')
	print(f'Iris: The current time is {Time}\n')
	speak(f"the current time is {Time}")

def date_now(speak):
	date = datetime.datetime.now().strftime('%d %B, %Y')
	print(f"Iris: Today's date is {date}\n")
	speak(f"today's date is {date}")