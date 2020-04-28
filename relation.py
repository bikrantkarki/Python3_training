#relation.py
# here the text insdie ''' or """ has information regarding the program code 
"""
Author: Bikrant Karki
Problem: input names and family relation
Target Users: all
Target System:GNU/Lnux
Interface:command line
Functional Requirements:Print out  character
                        get input
                        Print the input character name, description, gender and race
Testing:Simple run test
Maintainer: bikrantkarki.com.np || bikrant7@gmail.com

"""

#Assign
'''
here "" refer to the sting value
'''
myname=""
Name=""
Relation=""
more =""
divider= ".................********............"
#Take input
myname=input("Enter your Full Name:")
more=input("you want to continue yes or no \t ")
while (more == "yes") :
    Name =input("Enter full name of your relative:")
    Relation =input("Enter the relation with you:")
    #Print Output
    print(divider)
    print("\t Name  \t\t\t Relation with", myname)
    print("\t", Name,"\t\t\t",Relation)
    print(divider,"\n")
    more=input("do you want to add more? (yes or no)",)
