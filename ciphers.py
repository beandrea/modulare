class CustomError(Exception):
	pass

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

	alpha = [0]*26
	caps = [0]*26
	
	for i in range(97, 123):
		alpha[i - 97] = chr(i)
	
	for i in range(65, 91):
		caps[i - 65] = chr(i)

	result = ""
	for i in range(len(primer)):
		if primer[i].isdigit:
			raise CustomError("Digit entered in primer string")
		result +=  caps[(caps.index(primer[i]) + alpha.index(original[i])) % len(caps)]
		if (i + 1) % (pLen - 1) == 0:
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
	alpha = [0]*26
	caps = [0]*26
	
	for i in range(97, 123):
		alpha[i - 97] = chr(i)
	
	for i in range(65, 91):
		caps[i - 65] = chr(i)

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