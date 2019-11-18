#program demonstrating recurrsion.

def factorial(n):
    if n == 0:
        return 1
    else:
    # here the function is calling itself thus, called as a recurrsive function.
        return(n * factorial(n-1))

#number = input("Enter number:")
#print(factorial(number))
print(factorial(4))
