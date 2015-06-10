vowels = {'front_vowels': ['i', 'y', 'ɪ', 'ʏ', 'e', 'ø', 'ɛ', 'œ', 'æ', 'ɶ'],\
			'central_vowels': ['ɨ', 'ʉ', 'ɘ', 'ɵ', 'ə', 'ɜ', 'ɞ', 'ɐ'],\
			'back_vowels': ['ɯ', 'u', 'ø', 'ʊ', 'o', 'ɤ', 'ʌ', 'ɔ', 'ɑ', 'ɒ']}

consonants = {'bilabials': ['p','b','m','ʙ','ɸ'], 'labiodentals': ['ɱ','ⱱ','f','v','ʋ'], 'dentals': ['θ','ð'],\
			 'alveolar': ['t','d','n','r','ɾ','s','z','ɬ','ɮ','ɹ','l'], 'post-alveolar': ['ʃ','ʒ'],\
			  'retroflex': ['ʈ','ɖ','ɳ','ɽ','ʂ','ʐ','ɻ','ɭ'], 'palatals':['c','ɟ','ɲ','ç','ʝ','j','ʎ'],\
			  'velar':['k','g','ŋ','x','ɣ','ɰ','ʟ'], 'uvular':['q','ɢ','ɴ','ʀ','χ','ʁ'], 'pharyngeal':['ħ','ʕ'],\
			   'laryngeal':['ʔ','h','ɦ'], 'affricates': ['tʃ','dʒ']}

IPA = {'consonants': consonants, 'vowels': vowels}



def WordStructure(words):
	"""Takes in a list of words and returns their Vowel-Consonant
	cluster forms
	>>> x = ['kat']
	>>> WordStructure(x)
	['CVC']
	>>> y = ['kæliforniə']
	>>> WordStructure(y)
	['CVCVCVCCVV']
	"""


	# structure_list = []
	# for word in words:
	# 	structure_string = ""
	# 	for letter in word:
	# 		print (letter)

	# 		if letter in vowels.values():
	# 			structure_string +="V"
	# 		elif letter in consonants.values():
	# 			structure_string += "C"
	# 	structure_list.append(structure_string)
	# return structure_list
