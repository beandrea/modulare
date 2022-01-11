import ciphers

def promptAmsco():
	dOrE = input("Enter 'D' for decode or 'E' for encode: ").strip().lower()
	wrdLst = ["an encoded","an original"]
	print("Enter", wrdLst[0] if dOrE == "d" else wrdLst[1] if dOrE == "e" else "a valid", "string: ")
	original = input()
	key = input("Enter the amsco key in the form xyz, where the length of the key is, at most, one third the length of the string entered: ")
	
	print("Result is:", ciphers.amsco(key, original))

def promptAmsco(key, original):
	print("Result is:", ciphers.amsco(key, original))

def promptCaes():
	dOrE = input("Enter 'D' for decode or 'E' for encode: ").strip().lower()
	wrdLst = ["an encoded","an original"]
	print("Enter", wrdLst[0] if dOrE == "d" else wrdLst[1] if dOrE == "e" else "a valid", "string: ")
	original = input()
	shift = input ("Enter the shift value, positive or negative: ")

	print("Result is:", ciphers.caeser(original, shift))

def promptBlock():
	dOrE = input("Enter 'D' for decode or 'E' for encode: ").strip().lower()
	wrdLst = ["an encoded","an original"]
	print("Enter", wrdLst[0] if dOrE == "d" else wrdLst[1] if dOrE == "e" else "a valid", "string: ")
	original = input()
	blocks = input("Enter the block cipher in the format xyz:yxz ")
	
	print("Result is: \n", ciphers.blockCipher(original, blocks))

def switcher(op):
	if(op == 'caeser'):
		promptCaes()
	elif(op == 'block'):
		promptBlock()
	elif(op == 'amsco'):
		promptAmsco()
	elif(op == 'test'):
		promptAmsco('41325', 'Incomplete columnar with alternating single letters and digraphs')
	else:
		print("Invalid Entry")

switcher(input("What kind of cipher do you need to be run? Enter 'caeser', 'block', 'amsco', 'test': ").strip().lower())