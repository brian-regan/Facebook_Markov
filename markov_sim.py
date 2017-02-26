import json
import random

		
def add_to_dict(key, value, dic):
	if key in dic:
		dic[key].append(value)
	else:
		dic[key] = [value]

def make_makov_dict(messages):

	corpus = {}
	for message in messages:
		text = message['message']
		words = text.split()
		words.append("$end$")
		word_count = len(words)

		for i in range(word_count - 1):
			add_to_dict(words[i].lower(), words[i+1].lower(), corpus)

	return(corpus)

def make_message(seed, corpus):

	if seed in corpus:
		sentance = [seed]
		word = seed

		while word != '$end$':
			next_list = corpus[word]

			word = random.choice(next_list)
			sentance.append(word)

		print(' '.join(sentance))
	else:
		print('{0} not found in corpus'.format(seed))




def main():
	reply = ""
	with open('chat_dat.txt', encoding='utf8') as data_file:    
		data = json.load(data_file)

	threads = data['threads']

	# Here included the id's of the friends (incuding yourself)
	# that are in the relevant chat.
	
	user_ids = {
			'###@facebook.com' : 'name',
			'###@facebook.com' : 'name',
			'###@facebook.com' : 'name',
			'###@facebook.com' : 'name',
			'###@facebook.com' : 'name',
			'###@facebook.com' : 'name',
			'###@facebook.com' : 'name'
			}

	for thrd in threads:
		if set(user_ids.keys()) ==  set(thrd['participants']):
			chat = thrd
			print("\nFound Chat with {0}".format(' '.join(list(user_ids.values()))))
	
	corpus = make_makov_dict(chat['messages'])
	print("Created Corpus")

	print("Welcome to Message Simulator \n ------------------------ \n")

	while reply != "$exit$":
		reply = input("Input Seed Word: ")
		if reply != "$exit$":
			make_message(reply, corpus)


main()