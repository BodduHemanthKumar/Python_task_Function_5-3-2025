# Define Function
print("Define Function")
def greet():
    print("Hello, Good morning Hemanth!")
greet()
print(" ")

# Function with parameters
print("Function with parameters")
def greet(name):
    print("Hello, " + name)
greet("hemanth")
greet("Bob")
print(" ")

#Returning values from a function
print("Returning values from a function")
def add(a,b):
    return a+b
result = add(3,5)
print(result)
print(" ")

#Functions with multiple parameters
print("Functions with Multiple parameters")
def multiply(a,b,c):
    return a*b*c
result = multiply(2,3,4)
print(result)
print(" ")

#Lambda Function
print("lambda Function")
Square = lambda x: x**2
print(Square(4))
print(" ")
add=lambda a,b: a+b
print(add(3,5))