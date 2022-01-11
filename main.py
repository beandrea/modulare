import ciphers

def promptAmsco():
	dOrE = input("Enter 'D' for decode or 'E' for encode: ").strip().lower()
	wrdLst = ["an encoded","an original"]
	print("Enter", wrdLst[0] if dOrE == "d" else wrdLst[1] if dOrE == "e" else "a valid", "string: ")
	original = input()
	key = input("Enter the amsco key in the form xyz, where the length of the key is, at most, one third the length of the string entered: ")
	
	print("Result is: \n", ciphers.amsco(original, key))

def promptAutokey():
	dOrE = input("Enter 'D' for decode or 'E' for encode: ").strip().lower()
	wrdLst = ["an encoded","an original"]
	print("Enter", wrdLst[0] if dOrE == "d" else wrdLst[1] if dOrE == "e" else "a valid", "string: ")
	original = input()
	primer = input("Enter a primer string, letters only: ")
	if primer.isalpha():
		print("Result is: \n", ciphers.autokey(original, primer))
	else:
		print("Please only enter letters")

def promptBazeries():
	dOrE = input("Enter 'D' for decode or 'E' for encode: ").strip().lower()
	wrdLst = ["an encoded","an original"]
	print("Enter", wrdLst[0] if dOrE == "d" else wrdLst[1] if dOrE == "e" else "a valid", "string: ")
	original = input()
	key = input("Enter a number less than one million: ")
	print("Result is: \n", ciphers.bazeries(original, key))

def promptBazeries(original, key):
	print("Result is: \n", ciphers.bazeries(original, key))

def promptBlock():
	dOrE = input("Enter 'D' for decode or 'E' for encode: ").strip().lower()
	wrdLst = ["an encoded","an original"]
	print("Enter", wrdLst[0] if dOrE == "d" else wrdLst[1] if dOrE == "e" else "a valid", "string: ")
	original = input()
	blocks = input("Enter the block cipher in the format xyz:yxz ")
	
	print("Result is: \n", ciphers.blockCipher(original, blocks))

def promptCaes():
	dOrE = input("Enter 'D' for decode or 'E' for encode: ").strip().lower()
	wrdLst = ["an encoded","an original"]
	print("Enter", wrdLst[0] if dOrE == "d" else wrdLst[1] if dOrE == "e" else "a valid", "string: ")
	original = input()
	shift = input ("Enter the shift value, positive or negative: ")

	print("Result is: \n", ciphers.caeser(original, shift))

def switcher(op):
	if(op == 'amsco'):
		promptAmsco()
	elif(op == 'autokey'):
		promptAutokey()
	elif(op == 'bazeries'):
		promptBazeries()
	elif(op == 'block'):
		promptBlock()
	elif(op == 'caeser'):
		promptCaes()
	elif(op == 'test'):
		promptBazeries("Simple substitution plus transposition", "3752")
	else:
		print("Invalid Entry")

switcher(input("What kind of cipher do you need to be run? Enter 'amsco', 'autokey', 'bazeries', 'block', 'caeser', 'test': ").strip().lower())