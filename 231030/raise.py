# # Exception Handling Example 
# # program to raise an exception if the input is not a positive integer

# try:
# 	num = int(input("Enter a positive integer: "))
# 	if num <= 0:
# 		raise ValueError("That is not a positive number!")
# except ValueError as e:
# 	print(e)
	
# program to check if a number is positive

def square_root(num):
	if num < 0:
		raise ArithmeticError("Cannot find square root of negative numbers!")
	else:
	    return num ** 0.5

def main():
	try:
		n = int(input("Enter a number: "))
		result = square_root(n)
	except ArithmeticError as e:
		print(e)
	else:
		print("The square root of", n, "is", result)
main()
