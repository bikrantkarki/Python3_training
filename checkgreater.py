#checkgreater.py
#Calculation Series 1
'''
Author: Bikrant Karki
Task:Check the a,b,c which one is greater
        1. Take the input of three float value
        2. Take the Input of the user full name
        3. check the value of each number 
        4. Print the greater number and lowest number
        
Target user: Who want to learn Python
Target System:GNU/Linux
Interface:command line
Functional Requirement: 
Testing: Simple Run Test|| python3
Maintainer: bikrantkarki.com.np|| bikrant7@gmail.com
'''
#set the required variables
username =""
a= float
b= float
c=float
divider="-----------------------*******************-----------------------"

#get the input for the variables
username=input("enter your full name:")
a=float(input("enter your first number:"))
b=float(input("enter your second number:"))
c=float(input("enter your third number:"))

#Start to chek and print 
print("\t Welcome", username,"to the Number checking system.")
if a>b>c:
    print(divider)
    print("greater Number \t middle number \t lowest number")
    print(a, "\t\t\t", b, "\t\t", c)
    print(divider)
elif b>a>c:
    print(divider)
    print("greater Number \t middle number \t lowest number")
    print(b, "\t\t\t", a, "\t\t", c)
    print(divider)
elif c>a>b:
    print(divider)
    print("greater Number \t middle number \t lowest number")
    print(c, "\t\t\t", a, "\t\t", b)
    print(divider)
elif b>c>a:
    print(divider)
    print("greater Number \t middle number \t lowest number")
    print(b, "\t\t\t", c, "\t\t", a)
    print(divider)
elif c>b>a:
    print(divider)
    print("greater Number \t middle number \t lowest number")
    print(c, "\t\t\t", b, "\t\t", a)
    print(divider)
elif a>c>b:
    print(divider)
    print("greater Number \t middle number \t lowest number")
    print(a, "\t\t\t", c, "\t\t", b)
    print(divider)
else:
    print(divider)
    print("all are the equal number")
    print(a, "\t", b, "\t", c)
    print(divider)

'''
Output1:
enter your full name:Bikrant karki
enter your first number:23
enter your second number:43
enter your third number:13
	 Welcome Bikrant karki to the Number checking system.
-----------------------*******************-----------------------
greater Number 	 middle number 	 lowest number
43.0 			 23.0 		 13.0
-----------------------*******************-----------------------

Output2:
enter your full name:Bikrant karki
enter your first number:23
enter your second number:23
enter your third number:23
	 Welcome Bikrant karki to the Number checking system.
-----------------------*******************-----------------------
all are the equal number
23.0 	 23.0 	 23.0
-----------------------*******************-----------------------
'''
