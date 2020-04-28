#calculation1.py
#Calculation Series 1
'''
Author: Bikrant Karki
Task:curtain size and the cost calculation
        1. Take the input of current rate per meter
        2. Take the Input is the curtain for Door or Window?
        3. Take the input of Length and breadth for the curtain
        4. Print the total area of curtain size
        5. Calculate the Total cost =area x current rate
        6. Print the Total Cost for Cutain of Door or window 
        
Target user: Who want to learn Python
Target System:GNU/Linux
Interface:command line
Functional Requirement: 
Testing: Simple Run Test|| python3
Maintainer: bikrantkarki.com.np|| bikrant7@gmail.com
'''

#Set the variables
curtain=""
#length= float
#breadth= float
#rate = float
cost = float
area = float
more= ""
divider ="--------------**********------------------"
#prompt for user-defined information

rate = input("enter the current market rate for the curtain per meter:")
curtain= input("You are lokking curtain for Door or window?:")
length = input ("enter the Length for your curtain in meter:")
breadth= input ("enter the breadth for your curtain in meter:")

#Calculate according to the information
length= float(length) #should convert the input and define the type
breadth= float(breadth)
rate = float(rate)

area = length*breadth;
print("The toal area for", curtain, "is", area ,"square meter")
cost= rate * area;
print("The Total cost for the", curtain, "is","Rs.", cost)

print(divider)
print("\t Total Area \t\t Total Cost \t Location")
print("\t",area, "sqm" ,"\t\t", "Rs.",cost, "\t", curtain)
print(divider)

'''
Output:

enter the current market rate for the curtain per meter:250
You are lokking curtain for Door or window?:front hall door
enter the Length for your curtain in meter:1.5
enter the breadth for your curtain in meter:3.5
The toal area for front hall door is 5.25 square meter
The Total cost for the front hall door is Rs. 1312.5
--------------**********------------------
	 Total Area 		 Total Cost 	 Location
	 5.25 sqm 		 Rs. 1312.5 	 front hall door
--------------**********------------------

'''
