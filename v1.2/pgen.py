import random
import pyperclip

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
signs = '!@#$%&'

print '\n'

length = input('Password length: ')
num_input = input('How many numbers: ')
sign_input = input('How many signs: ')
password = ''
length -= num_input + sign_input

for c in range(length):
	password += random.choice(letters)
for d in range(num_input):
	password += random.choice(numbers)
for f in range(sign_input):
	password += random.choice(signs)

print '\n'
print "The Password is: " + password
	
pyperclip.copy(password)	

print "\nPassword Copied To Clipboard!"	
closeInput = raw_input("Press ENTER to exit...\n")
print ("Closing...")