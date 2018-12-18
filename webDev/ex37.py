# This code takes the square root of the number inputed

# imports module
from sys import argv
# says that argv should expect the run of the program and a user input in the terminal
script, arg = argv

# makes variable "n" to the user input
n = int(arg)

for i in range( 1, n ):
    
    # if the floor of the user input divided by "i" is the same as the user input AND if the mod of the user input is 0, print the floor of the user input divided by the "i"
    if n//i == i and n%i == 0:
        print(n//i)
        
        # exit(0) will be a good exit
        exit(0)
        
print(False)