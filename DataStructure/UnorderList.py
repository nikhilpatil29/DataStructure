"""
	Purpose: UnOrdered LinkList Implementation
	@author Nikhil Patil
"""
from LinkList import *
class UnorderList:

	list1 = LinkList()
	f = open('demo.txt','rw+')
	split_Word = f.read().split(" ")
	index = 0
	length = len(split_Word)
	while  index < length:
		list1.insertdata(str(split_Word[index]))
		index += 1
	list1.printList()
	word = raw_input("enter the word which you want to search\n")
	result = list1.search(word)
	if result:
		list1.deleteword(word)
		list1.printList()
	else:
		list1.insertdata(word)
		list1.printList()

	list1.updateList()

	# print f.read()
	f.close()

