# Python program to demonstrate sys.argv

import sys
  
print("This is the name of the program:",
       sys.argv[0])
print("Number of elements including the name of the program:",
       len(sys.argv))
print("Argument List:",
       str(sys.argv))
