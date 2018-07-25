'''
 Purpose: To find given Expression in balance or not
 @author Nikhil Patil

 '''
from Stack import *
class BalancePara:
    s = Stack()
    exp = raw_input('Please enter the expression: ')
    index = 0
    for c in exp:
    	
        if c == '(':
            s.push(c)
        elif c == ')':
            if s.is_empty():
                is_balanced = False
                break
            s.pop()
    else:
        if s.is_empty():
            is_balanced = True
        else:
            is_balanced = False
     
    if is_balanced:
        print('Expression is correctly parenthesized.')
    else:
        print('Expression is not correctly parenthesized.')
