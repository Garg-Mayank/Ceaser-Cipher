# Cipher Series
# Ceaser Cipher.

import garbage

def ceaserE(plain_Text, shift):			# Plain Text and Shifting Letters to Encrypt. 
	ciphertext = ''
	for letters in plain_Text: 
		if letters == ' ':
			ciphertext = ciphertext + letters
		elif  letters.isupper():
			ciphertext = ciphertext + chr((ord(letters) + shift - 65) % 26 + 65)
		else:
			ciphertext = ciphertext + chr((ord(letters) + shift - 97) % 26 + 97)
  
	return ciphertext
	
def ceaserD(cipher_Text, key):			# Plain Text and key to Decrypt. 
	plaintext = ''
	for letters in cipher_Text: 
		if letters == ' ':
			plaintext = plaintext + letters
		elif  letters.isupper():
			plaintext = plaintext + chr((ord(letters) - key - 65) % 26 + 65)
		else:
			plaintext = plaintext + chr((ord(letters) - key - 97) % 26 + 97)
  
	return plaintext
	
	
def user_opt(option):

	if option == 1:
		plain_Text = input("Enter Words to Encrypt: ")
		shift = int(input("Enter letters to shift: "))
		garbage.clrscr()
		print(ceaserE(plain_Text, shift))
		
	else:
		cipher_Text = input("Enter words to Decrypt: ")
		key = int(input('Enter Key: '))
		garbage.clrscr()
		print(ceaserD(cipher_Text, key))

		
option = int(input("What you want to do: \n1. Encrypt: \n2. Decrypt: \n"))
print(user_opt(option))
#print(ceaserE(plain_Text, shift))
