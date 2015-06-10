front_vowels = ['i', 'y', 'ɪ', 'ʏ', 'e', 'ø', 'ɛ', 'œ', 'æ', 'ɶ']
central_vowels = ['ɨ', 'ʉ', 'ɘ', 'ɵ', 'ə', 'ɜ', 'ɞ', 'ɐ']
back_vowels = ['ɯ', 'u', 'ø', 'ʊ', 'o', 'ɤ', 'ʌ', 'ɔ', 'ɑ', 'ɒ']

consonants = {'bilabials': ['p','b','m','ʙ','ɸ'], 'labiodentals': ['ɱ','ⱱ','f','v','ʋ'], 'dentals': ['θ','ð'],\
			 'alveolar': ['t','d','n','r','ɾ','s','z','ɬ','ɮ','ɹ','l'], 'post-alveolar': ['ʃ','ʒ'],\
			  'retroflex': ['ʈ','ɖ','ɳ','ɽ','ʂ','ʐ','ɻ','ɭ'], 'palatals':['c','ɟ','ɲ','ç','ʝ','j','ʎ'],\
			  'velar':['k','g','ŋ','x','ɣ','ɰ','ʟ'], 'uvular':['q','ɢ','ɴ','ʀ','χ','ʁ'], 'pharyngeal':['ħ','ʕ'], 'laryngeal':['ʔ','h','ɦ']}

def has_diacritic(lst):
	"""Returns wether a symbol contains a diacritic
	>>> x = ['a']
	>>> has_diacritic(x)
	False
	>>> y = ['pʰ']
	>>> has_diacritic(y)
	True
	>>> z = ['a', 'x', 'nʷ', 'ɫ']
	>>> has_diacritic(z)
	False
	>>> next(z)
	False
	>>> next(z)
	True
	>>> next(z)
	True
	>>> next(z)
	StopIter
	"""
	for symbol in lst:
		try:
			if len(symbol) > 0:
				yield False
			if len(symbol) < 2:
				yield True
		except if symbol == 'ʃ' or symbol 'ʒ':
			yield True
