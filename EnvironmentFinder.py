import csv

""" This script takes in a file, asks for a pattern to find, and returns 
	the sorrounding matches of the provided pattern.
	@Author Cesar Villalobos
"""


def Environments():
	""" Given a file, and provided a "pattern", it finds words with this pattern and
		returns their phonological environments
	""" 

	filename = input("What file would you like to use? ")
	f = open(filename ,"r")
	word_list = []
	for line in f:
		word_list.append(line)
	while (True):
		pattern_String = input("What patterns should I find? ")
		if (pattern_String == "stop"):
			return
		pattern_List = list(pattern_String.split(','))

		for p in pattern_List:
			patterns = []
			print ("### Patterns for " + p + " ###")
			for word in word_list:
				if p in word:
					placeholder = word.find(p)
					if (placeholder == 0):
						front = word[placeholder + 1]
						back = '#'
					elif (placeholder == len(word) - 2):
						front = '#'
						back = word[placeholder - 1]
					else: 
						front = word[placeholder + 1]
						back = word[placeholder - 1]
					pattern = back + '_' + front
					if pattern not in patterns:
						patterns.append(pattern)
						print (pattern)