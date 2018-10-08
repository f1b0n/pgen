import pyperclip

def manual():
	
	import random
	
	letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	numbers = '1234567890'
	signs = '!@#$%&'
	
	print "\n> > > The Formatting is:"
	print "> > > Length in Letters + Numbers + Signs."
	print "> > > Type 0 for the Main Menu."
	
	length = input('\nPassword length: ')
	if length == (0):
		main()
	else:
		num_input = input('How many numbers: ')
		sign_input = input('How many signs: ')
		password = ''
	
	if length >= (num_input + sign_input):
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
		exit()
	else:
		print "\nYour numbers don't add up xd"
		print "Try Again ^_^"
		manual()

def random():

	import random
	
	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&'

	print "\n> > > The Formatting is:"
	print "> > > Fully Randomized."
	print "> > > Type 0 for the Main Menu."
	
	length = input('\nPassword length: ')
	if length == (0):
		main()
	else:
		password = ''
		for c in range(length):
			password += random.choice(chars)
		print '\n'
		print "The Password is: " + password
			
		pyperclip.copy(password)
		
		exit()

def exit():
	
	print "\nPassword Copied To Clipboard!"	
	closeInput = raw_input("Press ENTER to exit...\n")
	print ("Closing...")

def main():
	print '\n'
	while True:
		choice = input('Manual (1) or Random (2) password generating method? > ')
		if choice == (1):
			manual()
		elif choice == (2):
			random()
		else:
			print "You can only select option 1 or 2."
			main()
		break
		
main()