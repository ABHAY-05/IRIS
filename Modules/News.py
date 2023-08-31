import requests
import json

def news(NEWS, speak, take_command, my_name):
	url = NEWS
	response = requests.get(url)
	data = json.loads(response.content)
	a=0
	def news_say(data, a):
		new=data['articles'][a]
		print("##############################################################\n")
		print(new['title'],"\n")
		speak(new['title'])
		print('______________________________________________________\n')
		print(new['description'],"\n")
		speak(new['description'])
		print("..............................................................\n")
		return new
	news_say(data, a)
	while True:
		speak('do you want to hear more news?')
		command=take_command()
		if 'yes' in command:
			a=a+1
			news_say(data,a)
		else:
			speak(f'okay {my_name()}')
			break