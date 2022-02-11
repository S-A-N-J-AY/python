# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:33:45 2022

@author: mandeep
"""

a=int(input("Enter the first Number: " ))
b=int(input("Enter the second number: " ))
o=input("Enter the operation: " )
if o== '+':
    s=a+b
    print("The sum of the numbers is: ",s)
elif o == '-':
    s=a-b
    print("The difference of the numbers is: ",s)
elif o == '*':
    s=a*b
    print("The product of the numbers is: ",s)
elif o == '/':
    if b!=0:
        s=a/b
        print("First number divided by the second number is: ",s)
    else:
        print("Division by zero error")
else:
    print("Invalid operation")