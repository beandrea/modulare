class CustomError(Exception):
	pass

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

def amsco(key, aStr):
	keys = list(str(key))
	size = int(len(aStr) / len(str(key)))
	aLst = [0]*size

	for i in range(len(aLst)):
		aLst[i] =  [0]*len(keys) 

	start = 0
	end = 2
	for i in range(len(aLst)):
		for j in range(len(aLst[0])):
			aLst[j][i] = aStr[start : end]
			start = end
			if end % 3 == 2:
				end += 1
			elif end % 3 == 0:
				end += 2

	result = ""
	for i in range(len(keys)):
		for j in range(len(aLst[0])):
			print(int(keys[i]) - 1)
			print(aLst[int(keys[i]) - 1][j])
			result += aLst[int(keys[i]) - 1][j]

	return result
