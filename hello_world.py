#hello_world.py
# here the text insdie ''' or """ has information regarding the program code 
"""
Auther: Bikrant Karki
Problem:get computer to output message
Target Users:Me
Target System:GNU/Lnux
Interface:command line
Functional Requirements:Print out message
                        get input
                        Print the input text or number
Testing:Simple run test
Maintainer: bikrantkarki.com.np || bikrant7@gmail.com

"""
#1. Print out a any message
print("Hello World!")
#2. Input some text
'''
you can place Doubble quote (") or single quote (')
inside input (" text") or input (' text ')
'''
some_text = input('What is your Name: ')
#3. Print our the text we just entered
print("welcome, " , some_text)

'''
    This Script can be run by typing
    $python3 hello_world.py
    
    if you choose $python hello_world.py
    it's gonna give you
    root:~$ python hello_world.py 
Hello World!
What is your Name: test
Traceback (most recent call last):
  File "hello_world.py", line 16, in <module>
    some_text = input('What is your Name: ')
  File "<string>", line 1, in <module>
NameError: name 'test' is not defined

So choosing the correct interpreter is important!
:-)

'''
