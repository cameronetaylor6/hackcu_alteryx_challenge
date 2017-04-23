import string

def getGroups(data, n):
	groups = {}
	for i in range(0, len(data), n):
		group = data[i:i+n]
		groups[group] = groups.get(group, 0) + 1
	#groupSizes = sorted(((v, k) for k, v in groups.items()), reverse=True)
	#print(groupSizes[0:10])
	return groups

def getMaxLengthOfAtLeastKOccurences(data, k):
	n = 2
	while(1):
		sizes = {}
		for i in range(0, len(data), n):
			size = data[i:i+n]
			sizes[size] = sizes.get(size, 0) + 1
		maximum = max(sizes, key=sizes.get)
		if(sizes[maximum] > k):
			n += 2
		else:
			print(maximum, sizes[maximum])
			break
	return n

def toEnglish(s):
	sentence = s.split(" ")
	english = ""
	for word in sentence:
		if word[:len(word) - 4:-1] == 'yaw':
			english += word[:len(word) - 3] + " "
		else: 
			noay = word[:len(word) - 2]
			firstconsonants = noay.split("a")[-1]
			consonantsremoved = noay[:len(noay) - (len(firstconsonants)+1)]
			english += firstconsonants + consonantsremoved + " "
	return english

def writeSolvedFile(data, decryptDict):
	solved = ""
	with open("solved.txt", "w") as f:
		for i in range(0, len(data), 2):
			pair = data[i:i+2]
			solved+=decryptDict[pair]
		#solved = toEnglish(solved)
		ays = ['yay', 'YAY', 'ay', 'AY']
		special = [" ", "?", "!", ".", ",", ":", ";", "\n", "'"]
		for ay in ays:
			for spec in special:
				solved = solved.replace(ay+spec, spec)

		consClust = ["wh", "WH", "cr", "CR", "th", "pl", "pr", "bl", "br", "tr", "dr", "kl", "kr", "gl", "gr", "fl", "fr", "or", "shr", "sk", "skr", "sl", "sm", "sn", "sp", "spl", "spr", "st", "str", "sw", "tw", "dw", "kw", "skw", "gw", "TH", "PL", "PR", "BL", "BR", "TR", "DR", "KL", "KR", "GL", "GR", "FL", "FR", "OR", "SHR", "SK", "SKR", "SL", "SM", "SN", "SP", "SPL", "SPR", "ST", "STR", "SW", "TW", "DW", "KW", "SKW", "GW"]
		vowels = ["a", "e", "i", "o", "u"]
		capVowels = ["A", "E", "I", "O", "U"]
		letters = list(string.ascii_lowercase)
		lettersCap = list(string.ascii_uppercase)


		split = solved.split(" ")
		newSolved = []

		for word in split:
			endl = False
			if(word[-1:] is '\n'):
				final = word.replace('\n', '')
				endl = True
			special = False
			if(word[-1:] not in letters and word[-1:] not in lettersCap):
				spec = word[-2:-1]
				word = word[:len(word)-2]
				special = True
			if(len(word) is 2 and word[:1] in vowels):
				word = word[1:2] + word[:1]
			elif(len(word) is 2 and word[:1] in capVowels):
				word = word[1:2].upper() + word[:1].lower()
			elif word[-1:] not in vowels:
				if word[-2:] in consClust and word[-3:-2] not in vowels and word[-3:-2] not in capVowels:
					end = word[:len(word)-2]
					begin = word[-2:]
				else:
					end = word[:len(word)-1]
					begin = word[-1:]
				if word[0:1] in capVowels and word is not word.upper():
					begin = begin.title()
					end = end.lower()
				word = begin+end
			if(special):
				speical = False
				word = word+spec
			if(endl):
				endl = False
				word = word+'\n'
			newSolved.append(word)
		newSolved = ' '.join(newSolved)

		f.write(newSolved)

def main():
	#26 letters x2, 10 numbers, 33, 95 total
	with open("Alteryx_CUHack2017.txt", "r") as f:
		data = f.read()
		singles = getGroups(data, 2)
		#pairs = getGroups(data, 4)
		#triples = getGroups(data, 6)
		solved = {}
		for key in singles:
			solved[key] = "~"
		# Lowercase Letters
		solved["ac"] = "a"
		solved["2c"] = "b"
		solved["3c"] = "c"
		solved["4c"] = "d"
		solved["5c"] = "e"
		solved["6c"] = "f"
		solved["7c"] = "g"
		solved["8c"] = "h"
		solved["9c"] = "i"
		solved["tc"] = "j"
		solved["jc"] = "k"
		solved["qc"] = "l"
		solved["kc"] = "m"
		solved["as"] = "n"
		solved["2s"] = "o"
		solved["3s"] = "p"
		solved["4s"] = "q"
		solved["5s"] = "r"
		solved["6s"] = "s"
		solved["7s"] = "t"
		solved["8s"] = "u"
		solved["9s"] = "v"
		solved["ts"] = "w"
		solved["js"] = "x"
		solved["qs"] = "y"
		solved["ks"] = "z"
		# CAPITAL LETTERS
		solved["aC"] = "A"
		solved["2C"] = "B"
		solved["3C"] = "C"
		solved["4C"] = "D"
		solved["5C"] = "E"
		solved["6C"] = "F"
		solved["7C"] = "G"
		solved["8C"] = "H"
		solved["9C"] = "I"
		solved["tC"] = "J"
		solved["jC"] = "K"
		solved["qC"] = "L"
		solved["kC"] = "M"
		solved["aS"] = "N"
		solved["2S"] = "O"
		solved["3S"] = "P"
		solved["4S"] = "Q"
		solved["5S"] = "R"
		solved["6S"] = "S"
		solved["7S"] = "T"
		solved["8S"] = "U"
		solved["9S"] = "V"
		solved["tS"] = "W"
		solved["jS"] = "X"
		solved["qS"] = "Y"
		solved["kS"] = "Z"		
		# Numbers
		solved["ah"] = "0"
		solved["2h"] = "1"
		solved["3h"] = "2"
		solved["4h"] = "3"
		solved["5h"] = "4"
		solved["6h"] = "5"
		solved["7h"] = "6"
		solved["8h"] = "7"
		solved["9h"] = "8"
		solved["th"] = "9"
		# Special
		solved["jh"] = "'"
		solved["kh"] = "\n"
		solved["aD"] = "&"
		solved["2D"] = "<"
		solved["3D"] = ">"
		solved["4D"] = "["
		solved["5D"] = "]"
		solved["6D"] = "_"
		solved["7D"] = "`"
		solved["8D"] = "|"
		solved["9D"] = "}"
		solved["ad"] = " "
		solved["2d"] = "."
		solved["3d"] = ","
		solved["4d"] = "?"
		solved["5d"] = ":"
		solved["6d"] = ";"
		solved["7d"] = "!"
		solved["8d"] = "("
		solved["9d"] = ")"
		solved["td"] = "-"
		solved["kd"] = "\""
		solved["\n"] = ""

		writeSolvedFile(data, solved)

if __name__ == "__main__":
	main()
'''

~2h~7h~ah~th
 
~5C~7S~8C~aC~qS ~2S~aS~aS~5C~7S~6S~6S~aC~qS
 
y~2cay ~9C~qc~qc~9ca~kc~tsay ~aC~jc~5c~6s~3s~5ca~5s~5c~6s~8cay

~2h~7h~ah~th
 
~5C~7S~8C~aC~qS ~2S~aS~aS~5C~7S~6S~6S~aC~qS
 
y~2cay ~9C~qc~qc~9ca~kc~tsay ~aC~jc~5c~6s~3s~5ca~5s~5c~6s~8cay

'''