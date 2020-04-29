#functiontype.py
#Calculation Series 1
'''
Author: Bikrant Karki
Task: add two number with function return type and non-return type
        
Target user: Who want to learn Python
Target System:GNU/Linux
Interface:command line
Functional Requirement: 
Testing: Simple Run Test|| python3
Maintainer: bikrantkarki.com.np|| bikrant7@gmail.com
'''

#defining the functin name add_r which is retrun type
def add_r(a,b):
    x= a+b
    return x    #it return the value of x

#defining the function name add_n which is non-return type
def add_n(a,b):
    x=a+b
    print("and the sum is:",x)
#Prompt the user-define value for n1 and n2
n1=float(input("Enter 1st number:"))
n2=float(input("Enter 2nd number:"))

print("your numers are,",n1,n2)
#function call non-return type
add_n(n1,n2)
#function call for retrun type, if we don't use print the value wont be shown
print("And the sum is:",add_r(n1,n2))

'''
Output:
Enter 1st number:3445
Enter 2nd number:3332
your numers are, 3445.0 3332.0
and the sum is: 6777.0
And the sum is: 6777.0
'''
