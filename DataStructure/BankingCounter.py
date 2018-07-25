'''
 Purpose: Banking operation using Queue
 @author Nikhil Patil

 '''
from Queue import *
class BankingCounter:

	bankBalance = 10000
	size = int(input("Enter a size of queue\n"))

	people = int(input("Enter number of people in queue\n"))

	obj = Queue(size, people)

	while 1:
		print("1:Deposite a money")
		print("2:withdrawal a money")
		print("3:check your bank balance ")
		print("4:number of person in a queue")
		print("5:Dequeue a person")
		print("6:Add person in queue")
		print ("7.Exit")

		choice = int(input("\nenter your choice\n"))

		if choice == 1:
			print("Enter deposite money :")
			money = input()
			bankBalance=bankBalance+money
			print("BankBalance is :",bankBalance)

		elif choice == 2:
			print("Enter widrawal amount")
			widraw = input()
			if(widraw > bankBalance):
				print("insufficient balance")
			bankBalance =bankBalance-widraw
			print("Balance is :",bankBalance)

		elif choice == 3:
			print("Current balance is: ",bankBalance)

		elif choice == 4:
			NoOfPeople=obj.NumOfPeople()
			print "number of people in a queue is ",NoOfPeople

		elif choice == 5:
			obj.Deque()
			NumOfPeople=obj.NumOfPeople()
			print("number of person remaining in queue ",NumOfPeople)
		elif choice == 6:
			obj.Enque()
			NumOfPeople=obj.NumOfPeople()
			print("number of person remaining in queue ",NumOfPeople)

		elif choice == 7:
			exit(0)
		else:
			print "Please enter the choice between 1 to 7"
