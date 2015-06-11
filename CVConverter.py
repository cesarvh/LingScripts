# vowels = {'front_vowels': ['i', 'y', 'ɪ', 'ʏ', 'e', 'ø', 'ɛ', 'œ', 'æ', 'ɶ'],\
# 			'central_vowels': ['ɨ', 'ʉ', 'ɘ', 'ɵ', 'ə', 'ɜ', 'ɞ', 'ɐ'],\
# 			'back_vowels': ['ɯ', 'u', 'ø', 'ʊ', 'o', 'ɤ', 'ʌ', 'ɔ', 'ɑ', 'ɒ']}
vowels = ['ɯ', 'u', 'ø', 'ʊ', 'o', 'ɤ', 'ʌ', 'ɔ', 'ɑ', 'ɒ', 'i', 'y', 'ɪ', 'ʏ',
		  'e', 'ø', 'ɛ', 'œ', 'æ', 'ɶ', 'ɨ', 'ʉ', 'ɘ', 'ɵ', 'ə', 'ɜ', 'ɞ', 'ɐ', 'a']
consonants = ['p','b','m','ʙ','ɸ','ɱ','ⱱ','f','v','ʋ','θ','ð',
			 't','d','n','r','ɾ','s','z','ɬ','ɮ','ɹ','l','ʃ','ʒ'
			 'ʈ','ɖ','ɳ','ɽ','ʂ','ʐ','ɻ','ɭ', 'c','ɟ','ɲ','ç','ʝ','j','ʎ',
			  'k','g','ŋ','x','ɣ','ɰ','ʟ', 'q','ɢ','ɴ','ʀ','χ','ʁ', 'ħ','ʕ',
			   'ʔ','h','ɦ','tʃ','dʒ']

# IPA = {'consonants': consonants, 'vowels': vowels}



def WordStructure():
	"""Takes in a list of words and returns their Vowel-Consonant
	cluster forms
	>>> x = ['kat']
	>>> WordStructure(x)
	['CVC']
	>>> y = ['kæliforniə']
	>>> WordStructure(y)
	['CVCVCVCCVV']
	"""
	ans = input("Please enter file name: ")
	f = open(ans, "r")
	for line in f:
		structure = ""
		for letter in line:
			if letter in vowels:
				structure += "V"
			if letter in consonants:
				structure += "C"
		print (structure)
