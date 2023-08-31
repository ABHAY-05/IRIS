from pywikihow import search_wikihow

def wikihow(how, speak):
	try:
		max_results=1
		how_to=search_wikihow(how, max_results)
		assert len(how_to)==1
		how_to[0].print()
		speak(how_to[0].summary)
	except Exception as e:
		print(e)
		speak('sorry unable to find on wikihow')