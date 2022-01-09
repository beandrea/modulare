import ciphers

def promptCaes():
	dOrE = input("Enter 'D' for decode or 'E' for encode: ").strip().lower()
	wrdLst = ["encoded","original"]
	print("Enter the", wrdLst[0] if dOrE == "d" else wrdLst[1] if dOrE == "e" else "valid", "string: ")
	original = input()
	shift = input ("Enter the shift value, positive or negative: ")

	print("Result is:", ciphers.caeser(original, shift))

def promptBlock():
	dOrE = input("Enter 'D' for decode or 'E' for encode: ").strip().lower()
	wrdLst = ["encoded","original"]
	print("Enter the", wrdLst[0] if dOrE == "d" else wrdLst[1] if dOrE == "e" else "valid", "string: ")
	original = input()
	blocks = input("Enter the block cipher in the format xyz:yxz ")
	
	print("Result is: \n", ciphers.blockCipher(original, blocks))

def switcher(op):
	if(op == 'caeser'):
		promptCaes()
	elif(op == 'block'):
		promptBlock()
	elif(op == 'amsco'):
		exit()
	else:
		print("Invalid Entry")

switcher(input("What kind of cipher do you need to be run? Enter 'caeser', 'block', 'amsco': ").strip().lower())
