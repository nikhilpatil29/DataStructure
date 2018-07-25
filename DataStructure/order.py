"""
	Purpose: Ordered LinkList Implementation
	@author Nikhil Patil
"""
from LinkedListOrder import *
class order:
    file = open("Integer.txt","r+")

    number = file.read().split(" ")
    print number

    for i in range(0,len(number)):
        for j in range(0,len(number)-1):
            if number[j] > number[j+1]:
                temp = number[j]
                number[j] = number[j+1]
                number[j+1] = temp
    print number
    index = 0
    list1 = LinkedListOrder()
    while index < len(number):
        list1.insertdata(number[index])
        index += 1
    list1.printList()
