#normalcalculator.py
#use of function
'''
Author: Bikrant Karki
Task: To perform normal calculation of any two number
      1. define addition function and take two argument
      2. define substraction function and take two argument
      3. define multiply function and take two argument
      4. define division function and take two argument
      5. ask user to enter value for x
      6. ask user to enter value for y
      7. ask user for the task they want to perform, (add, sub , mul or div)?
      8. print the desired function
      9. ask for more calculation ?
      10. if yes reapeat 5
      11. if no end
arget user: Who want to learn Python
Target System:GNU/Linux
Interface:command line
Functional Requirement: 
Testing: Simple Run Test|| python3
Maintainer: bikrantkarki.com.np|| bikrant7@gmail.com
'''
#assign divider
divider ="-----------------#####################-----------------"

#define function with name addition
def addtion(a,b):
    return a+b
    
#define function with name substraction
def substraction(a,b):
    return a-b
#define function with name division
def division(a,b):
    return a/b
#define function with name multiplication
def multiplication(a,b):
    return a*b

#print the condtion for the operation
print(divider)
print("Please enter the number of the operation shown below")
print("\t 1 for Addition")
print("\t 2 for substraction")
print("\t 3 for multiplication")
print("\t 4 for division")
print(divider)
#get the user input
repeat=""
myname=""
myname =input("Please enter your full Name")
repeat= input("want to do calculation: (yes or no):")
while repeat == "yes":
    
    process = int(input("What would you like to do ?"))    
             
    x=float(input("Enter the value of a:"))
    y=float(input("Enter the value of b:"))


    if process == 1:
        print(divider)
        print("Dear,",myname,"your addition is:")
        print(x,"+",y,"=",addtion(x,y))
        print(divider)
    
    elif process == 2:
        print(divider)
        print("Dear,",myname,"your difference is:")
        print(x,"+",y,"=",substraction(x,y))
        print(divider)
        
    elif process == 3:
        print(divider)
        print("Dear,",myname,"your Multiplication is:")
        print(x,"*",y,"=",multiplication(x,y))
        print(divider)
        
    elif process == 4:
        print(divider)
        print("Dear,",myname,"your Division is:")
        print(x,"/",y,"=",division(x,y))
        print(divider)
    else:
        print(divider)
        print("!!!Invalid Input!!!")
        print(divider)
    
    repeat= input("want to do more calculation: (yes or no):")

'''
Output:

-----------------#####################-----------------
Please enter the number of the operation shown below
	 1 for Addition
	 2 for substraction
	 3 for multiplication
	 4 for division
-----------------#####################-----------------
Please enter your full NameMr. Bikrant Karki
want to do calculation: (yes or no):yes
What would you like to do ?4
Enter the value of a:55534
Enter the value of b:332
-----------------#####################-----------------
Dear, Mr. Bikrant Karki your Division is:
55534.0 / 332.0 = 167.2710843373494
-----------------#####################-----------------
want to do more calculation: (yes or no):yes
What would you like to do ?3
Enter the value of a:464
Enter the value of b:322
-----------------#####################-----------------
Dear, Mr. Bikrant Karki your Multiplication is:
464.0 * 322.0 = 149408.0
-----------------#####################-----------------
want to do more calculation: (yes or no):no
'''
