import psutil
def cpu(speak):
	usage = str(psutil.cpu_percent())
	speak('CPU is at'+ usage)
	print(f'cpu: {usage}')
	battery = psutil.sensors_battery()
	speak("Battery is at")
	speak(battery.percent )
	print(f'Battery: {battery.percent}')