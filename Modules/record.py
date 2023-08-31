import sounddevice as sd
from scipy.io.wavfile import write

def recsound(filename, speak, take_command):
	try:
		fs=44100
		speak("what should be the length of your sound wave please answer in seconds")
		seconds=int(take_command())
		recorded=sd.rec(int(seconds*fs),samplerate=fs,channels=2)
		sd.wait()
		write(f'files\\recordings\\{filename}.mp3',fs,recorded)
		speak("successfully recorded and saved")
	except Exception as e:
		print(f'{e}\n')