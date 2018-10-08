import random
import pyperclip

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&'
#numbers = '13'

#n = input('number of passwords: ')
#n = int(n)
print '\n'
length = input('Password length: ')
#length = random.choice(numbers)
#length = int(length)

#for p in range(n):
password = ''
for c in range(length):
	password += random.choice(chars)
print '\n'
print "The Password is: " + password
	
pyperclip.copy(password)	

print "\nPassword Copied To Clipboard!"	
closeInput = raw_input("Press ENTER to exit...\n")
print ("Closing...")