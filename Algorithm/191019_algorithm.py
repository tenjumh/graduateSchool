#순환(Recursion)

#Factorial
def factorial(n):
    #stop node
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))

