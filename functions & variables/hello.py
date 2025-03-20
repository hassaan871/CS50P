# print("hello, world")

# x = 10
# x = 'this is a string'

# y = "say, hello"

# x = str(3)
# y = int(3)
# z = float(3)

# print(type(y))
# y = 'name'

# Y = str("this is capital Y")
# print(Y)
# print(type(Y))

# print(type(x))
# print(type(y))
# print(type(z))

# Camel Case
myVariableName = "John"
# Pascal Case 
MyVariableName = "John"
# Snake Case 
my_variable_name = "John"

# print(myVariableName)
# print(MyVariableName)
# print(my_variable_name)

x, y, z = "Organe", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

x = y = z = "Django"
# print(x)
# print(y)
# print(z)

fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
# print(x)
# print(y)
# print(z)

fruits = ["apple", "mango", "banana", "cherry"]
x, *y, z = fruits
# print(x)
# print(y)
# print(type(y))
# print(z)
# print(x, y, z)

x = "Python"
y = " is "
z = "awesome"
# print(x + y + z)

x = 5
y = 10
# print(x + y)

x = 5
y = "John"
# print(x + y)
# print(x, y)

# Global variable
# x = "awesome"

# def myfunc():
#     x = "fantastic"
#     print("Python is " + x)

# myfunc()

# print("Python is " + x)

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)