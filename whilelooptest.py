#whilelooptest.py
'''
Author: Bikrant Karki
Task: Create loop
Target user: Who want to learn Python while loop
Target system: GNU/Linux
Interface:  command Line
Functional requirement: --
Testing: Simple Run Test|| python 3
Maintainer: bikrantkarki.com.np||bikrant@gmail.com
'''
'''
while :
while with small 'w' is keyword of python to create a loop until given condition is true.
syntax of while:
while a >=100:
    a -=100
    print (result)

'''

#get the test variable
test =1 #we have assign test with value 1

#make a while statement
while test < 1000:  #here test will be check if its lessthan 1000 or not
    test *= 2       #here test is multiply by 2 each time when its enter in the loop
    print(test)     #here test value is printed until it satisfy the condition

'''
Output:
2
4
8
16
32
64
128
256
512
1024
'''
