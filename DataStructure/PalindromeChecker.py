"""
	Purpose : Program to find the given String is Palindrom or not
	using Deque
	@author Nikhil Patil
"""
from Dequeue import *
class PalindromeChecker:

	obj = Dequeue()

	string = raw_input("enter the string\n")

	for ch in string:
		obj.addRear(ch)
	str1 = ""
	for c in string:
		str1 = str1+obj.removeRear() 

	if(str1 == string):
		print "string is Palindrome"
	else:
		print "string is not Palindrome"
