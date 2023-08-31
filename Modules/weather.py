import requests

def weather(city_name, WEATHER, speak, take_command):
	if all(word in city_name for word in ['today','weather','of']) or all(word in city_name for word in ['report','weather','of']) or all(word in city_name for word in ['report','weather','in']) or all(word in city_name for word in ['today','weather','in']):
		api_key = WEATHER
		base_url = "http://api.openweathermap.org/data/2.5/weather?"
		city_name = city_name.replace("today's",'').replace('iris','').replace('weather','').replace('of','').replace('in','').replace('report','').replace(' ','').strip()
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name
		response = requests.get(complete_url)
		x = response.json()
		if x["cod"] != "404":
			y = x["main"]
			current_temperature =format(y["temp"] - 273.15,'0.2f')
			current_pressure = y["pressure"]
			current_humidiy = y["humidity"]
			z = x["weather"]
			weather_description = z[0]["description"]
			print("Iris: Temperature (in celcius unit) = " +
						str(current_temperature) +
			"\nIris: atmospheric pressure (in hPa unit) = " +
						str(current_pressure) +
			"\nIris: humidity (in percentage) = " +
						str(current_humidiy) +
			"\nIris: description = " +
						str(weather_description))
			print('\n')
			speak("Temperature in celcius unit: " + str(current_temperature) + ".  atmospheric pressure in hPa unit: " + str(current_pressure) + ".   humidity in percentage :" + str(current_humidiy) + ".   description : " + str(weather_description))

		else:
			speak('city not found')

	else:
		api_key = WEATHER
		base_url = "http://api.openweathermap.org/data/2.5/weather?"
		speak('what is name of your city?')
		city_name = take_command().strip()
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name
		response = requests.get(complete_url)
		x = response.json()
		if x["cod"] != "404":
			y = x["main"]
			current_temperature =format(y["temp"] - 273.15,'0.2f')
			current_pressure = y["pressure"]
			current_humidiy = y["humidity"]
			z = x["weather"]
			weather_description = z[0]["description"]
			print("Iris: Temperature (in celcius unit) = " +
						str(current_temperature) +
			"\nIris: atmospheric pressure (in hPa unit) = " +
						str(current_pressure) +
			"\nIris: humidity (in percentage) = " +
						str(current_humidiy) +
			"\nIris: description = " +
						str(weather_description))
			print('\n')
			speak("Temperature in celcius unit: " + str(current_temperature) + ".  atmospheric pressure in hPa unit: " + str(current_pressure) + ".   humidity in percentage :" + str(current_humidiy) + ".   description : " + str(weather_description))

		else:
			speak('city not found')