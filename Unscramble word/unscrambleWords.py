#Unscrable the word

file = open("wordlist.txt", "r").readlines()
input = open("inp.txt", "r").readlines()

def checking():
	list = []
	for Wordlist_word, Input_word in enumerate(range(1)): #Have to use enumerate because of iterating two lists
		for Input_word in input:
			Input_word = Input_word.rstrip()
			for Wordlist_word in file:
				Wordlist_word = Wordlist_word.rstrip()
				veryList = []
				veryList2 = []
				wordVery = 0
				for char in Wordlist_word:
					if char in Input_word:
						veryList.append(char)
						wordVery = wordVery + 1
					else:
						break

				for char in Input_word:
					if char in Wordlist_word:
						veryList2.append(char)
						wordVery = wordVery + 1
					else:
						break

				if wordVery == len(Wordlist_word)*2: #Check if the word has the same length as the safetly wordVery variable
					if len(Wordlist_word) == len(Input_word):
							if sorted(veryList) == sorted(veryList2):
								list.append(Wordlist_word)
	return list

def format(list):
	for i in range(len(list)):
		if i < len(list)-1:
			print(list[i] + ",", end=' ')
		else:
			print(list[i], end='')

format(checking())


	# list = []
	# for Wordlist_word, Input_word in enumerate(range(1)): #Have to use enumerate because of iterating two lists
	# 	for Wordlist_word in file: # Every word of the wordlist
	# 		Wordlist_word = Wordlist_word.rstrip()
	# 		#print("Wordlist word: " + Wordlist_word)
	# 		for Input_word in input: # Every word in the input
	# 			Input_word = Input_word.rstrip()
	# 			wordVery = 0
	# 			#print("Input word: " + Input_word)
	# 			for char in Input_word: #Every character in the input
	# 				#print("Is " + char + " in " + Wordlist_word)
	# 				if char in Wordlist_word: # if the character is in the wordlist word
	# 					wordVery = wordVery + 1
	# 				else:
	# 					break
	#
	# 			if wordVery == len(Wordlist_word): #Check if the word has the same length as the safetly wordVery variable
	#
	# 				list.append(Wordlist_word)
	# return list
