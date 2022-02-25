class CustomError(Exception):
	pass

alpha = [0]*26
caps = [0]*26
	
for i in range(97, 123):
	alpha[i - 97] = chr(i)
	
for i in range(65, 91):
	caps[i - 65] = chr(i)

def numToEN(num):
	num = int(num)
	if(num < 0):
		raise CustomError("Number cannot be less than zero")

	aDict = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 
		7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'eleven', 12 : 'twelve', 
		13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 
		18 : 'eighteen', 19 : 'nineteen', 20 : 'twenty', 30 : 'thirty', 40 : 'forty', 
		50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}

	if(num < 20):
		return aDict[num]
	elif(num < 100):
		if(num % 10 == 0):
			return aDict[num]
		else: 
			return aDict[num // 10 * 10] + "" + aDict[num % 10]
	elif(num < 1000):
		if num % 100 == 0: 
			return aDict[num // 100] + "hundred"
		else: 
			return aDict[num // 100] + "hundredand" + numToEN(num % 100)
	elif(num < (1000 * 1000)):
		if num % 1000 == 0: 
			return numToEN(num // 1000) + "thousand"
		else: 
			return numToEN(num // 1000) + "thousand" + numToEN(num % 1000)
	else:
		raise CustomError("Number cannot be larger than 1,000,000")

def amsco(aStr, key):
	aStr = "".join(aStr.split())
	keys = list(str(key))
	size = int(len(aStr) / len(str(key)))
	aLst = [0]*len(keys)

	for i in range(len(aLst)):
		aLst[i] =  [0]*(size - 1) 

	start = 0
	end = 2
	for j in range(len(aLst[0])):
		for i in range(len(aLst)):
			aLst[i][j] = aStr[start : end]
			start = end
			if end % 3 == 2:
				end += 1
			elif end % 3 == 0:
				end += 2

	result = ""
	for i in range(len(keys)):
		for j in range(len(aLst[0])):
			result += aLst[keys.index(str(i + 1))][j]

	return result

def autokey(original, primer):
	pLen = len(primer)

	original = "".join(original.split(", "))
	original = "".join(original.split()).lower()
	primer += original
	primer = "".join(primer.split())[0:len(original)].upper()

	result = ""
	for i in range(len(primer)):
		if primer[i].isdigit:
			raise CustomError("Digit entered in primer string")
		result +=  caps[(caps.index(primer[i]) + alpha.index(original[i])) % len(caps)]
		if (i + 1) % (pLen - 1) == 0:
			result += " "

	return result

def bazeries(original, key):	
	'''sets the whole entered string to lower case for simplicity, then turns it into a list without spaces'''
	original = original.lower()
	original = list("".join(original.split()))
	
	'''turns key number into english letters, then sets it up to a list and adds any missed letters in 
		alphabetical order'''
	orgKey = key
	key = list(numToEN(key).upper())
	tmp = []
	for e in key:
		if e not in tmp:
			tmp.append(e)

	key = tmp
	
	alfa = [0]*25
	
	for i in range(97, 106):
		alfa[i - 97] = chr(i)
	for i in range(107, 123):
		alfa[i - 98] = chr(i)	
	for i in range(65, 73):
		if chr(i) not in key:
			key.append(chr(i))
	for i in range(75, 91):
		if chr(i) not in key:
			key.append(chr(i))

	result = ""
	move = list(str(orgKey))
	moveIn = 0
	for i in range(0, len(original), int(move[moveIn])):
		temp = original[i: (i + int(move[moveIn]))]
		temp.reverse()
		moveIn += 1

		if moveIn == len(move):
			moveIn == 0
			
		for let in temp:
			tmp = key[alfa.index(let)]
			result += tmp
			if len(result) % 6 == 5:
				result += " "
	return result
	
def blockCipher(aStr, cipher):
	if(not(":" in cipher)):
		raise CustomError("Invalid formatting")

	blockOne = list(cipher[: cipher.index(":")])
	blockTwo = list(cipher[cipher.index(":") + 1:])

	if(not(len(blockOne) == len(blockTwo))):
		raise CustomError("Cipher must have equal length on both sides")

	for i in range(len(blockOne)):
		blockOne[i] = int(blockOne[i]) - 1

	for i in range(len(blockTwo)):
		blockTwo[i] = int(blockTwo[i]) - 1	

	coded = [0]*len(aStr)

	for i in range(0, len(aStr), len(blockOne)):
		for j in range(0, len(blockOne)):
			coded[blockOne[j] + i] = aStr[blockTwo[j] + i]

	result = ""
	for let in coded:
		result += let
		
	return result

def caeser(aStr, offset):
	result = ""
	
	for i in range(len(aStr)):
		if(aStr[i] in alpha):
			place = alpha.index(aStr[i]) + (int(offset) % 25)

			if place > 25 and place % 25 != 0:
				place = place % 25
			elif place > 25 and place % 25 == 0:
				place = 25
		
			result += alpha[place]
		else:
			place = caps.index(aStr[i]) + (int(offset) % 25)

			if place > 25 and place % 25 != 0:
				place = place % 25
			elif place > 25 and place % 25 == 0:
				place = 25
		
			result += caps[place]
	return result