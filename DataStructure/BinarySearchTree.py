# Function to find the factorization of given number
# @param ele
# return
def facto(ele):
    facto = 1
    while ele > 1:
        facto = facto * ele
        ele -= 1
    return facto

# Program to find number of Node to form in a Binary Search Tree
# @author Nikhil Patil
class BinarySearchTree:

    number = int(input("enter the number\n"))

    count = 0
    list =[]

    while len(list) < number:
        ele = input("Enter your Item to the List: ")
        list.append(ele)
        print list
    i = 0
    while i < len(list):

        a = facto(2 * list[i])
        b = facto((list[i]+1))
        c = facto(list[i])
        count = a/(b*c)
        print "No. of nodes is ",list[i],"------>  No. of tree is ",count
        i += 1
        #
        # a = fact(2) * list[i]
        # b = fact(list[i] + 1)
        # c = fact(list[i])
        #
        # count = a / (b * c)
        # print count

