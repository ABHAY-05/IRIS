from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response
from chatterbot.trainers import ChatterBotCorpusTrainer

def chatbot():
	bot= ChatBot(name='Iris',read_only = True,
				storage_adapter="chatterbot.storage.SQLStorageAdapter",
				database_uri='sqlite:///database.sqlite3_eng',
				response_selection_method=get_random_response,
				logic_adapters=[
		{'import_path': 'chatterbot.logic.BestMatch',
		'default_response': 'sorry, i am not able to understand.',
		'maximum_similarity_threshold' : 0.50 ,
		'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance',
		},
		'chatterbot.logic.MathematicalEvaluation',
	],
	preprocessors=[
		'chatterbot.preprocessors.clean_whitespace',
		'chatterbot.preprocessors.unescape_html',
		'chatterbot.preprocessors.convert_to_ascii'
	]
	)
	trainer = ChatterBotCorpusTrainer(bot)
	trainer.train("files\\chats")
	return bot