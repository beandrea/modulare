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

	d = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 
		7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'eleven', 12 : 'twelve', 
		13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 
		18 : 'eighteen', 19 : 'nineteen', 20 : 'twenty', 30 : 'thirty', 40 : 'forty', 
		50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}

	if(num < 20):
		return d[num]
	elif(num < 100):
		if(num % 10 == 0):
			return d[num]
		else: 
			return d[num // 10 * 10] + "" + d[num % 10]
	elif(num < 1000):
		if num % 100 == 0: 
			return d[num // 100] + "hundred"
		else: 
			return d[num // 100] + "hundredand" + numToEN(num % 100)
	elif(num < 1000000):
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
	original = list("".join(original.split()))
	key = numToEN(key).upper()
	temp = []

	[temp.append(x) for x in key if x not in temp]
	key = temp	
	
	return ""
	
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