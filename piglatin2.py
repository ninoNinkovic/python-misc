def pigLatin(sentence):
	def _pigWord(word, suffix=""):
		if not word:
			if suffix:
				return suffix + "-yay"
			return ""
		if "-" in word:
			return "-".join(map(pigLatin, word.split("-")))
		if word[:2].lower() == "qu":
			return _pigWord(word[2:], word[:2])
		if word.isupper() and (suffix.isupper() or not suffix):
			return _pigWord(word.lower(), suffix).upper()
		if word.istitle() and not suffix or suffix.istitle() and word.islower():
			return _pigWord(word.lower(), suffix).capitalize()
		if word[0] in "AEIOUaeiou":
			if suffix:
				return word + "-" + suffix + "ay"
			return word + "-yay"
		return _pigWord(word[1:], suffix + word[0])
	WORD_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-"
	ans = buffer = ""
	for i in range(len(sentence)):
		c = sentence[i]
		if c in WORD_CHARS:
			buffer += c
		if c not in WORD_CHARS or i == len(sentence) - 1:
			ans += _pigWord(buffer)
			buffer = ""
		if c not in WORD_CHARS:
			ans += c
	return ans


print pigLatin("taco bell")
