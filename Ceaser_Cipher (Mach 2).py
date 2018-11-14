# Taking a file input to encrypt.

import garbage

def ceaserE(plain_Text, shift):			# Plain Text and Shifting Letters to Encrypt. 
	ciphertext = ''
	for letters in plain_Text: 
		#if letters == ' ':
		#ciphertext = ciphertext + letters
		if  letters.isupper():
			ciphertext = ciphertext + chr((ord(letters) + shift - 65) % 26 + 65)
		elif letters.islower():
			ciphertext = ciphertext + chr((ord(letters) + shift - 97) % 26 + 97)
		else:
			ciphertext = ciphertext + letters
		
	output_file.write(ciphertext)
	return ciphertext
	
def ceaserD(cipher_Text, key):			# Plain Text and key to Decrypt. 
	
	plaintext = ''
	for letters in cipher_Text: 
		#if letters == ' ':
		#	plaintext = plaintext + letters
		if  letters.isupper():
			plaintext = plaintext + chr((ord(letters) - key - 65) % 26 + 65)
		elif letters.islower():
			plaintext = plaintext + chr((ord(letters) - key - 97) % 26 + 97)
		else:
			plaintext = plaintext + letters
			
	output_file.write(plaintext)
	return plaintext

# Asking user whether s/he wants to ENCRYPT or DECRYPT	
def user_opt(option):

	if option == 1:
		plain_Text = words
		shift = int(input("Enter letters to shift: "))
		garbage.clrscr()
		print(ceaserE(plain_Text, shift))
		
	else:
		cipher_Text = words
		key = int(input('Enter Key: '))
		garbage.clrscr()
		print(ceaserD(cipher_Text, key))

# File Input.
name = input('File Name: ')
input_file = open(name, 'r')
words = input_file.read()
output_file = open('result.txt', 'w')

option = int(input("What you want to do: \n1. Encrypt: \n2. Decrypt: \n"))
print(user_opt(option))

"""
output_file = open('result.txt', 'w')
if option == 1:
	output_file.write(ciphertext)
else:
		output_file.write(plaintext)
"""