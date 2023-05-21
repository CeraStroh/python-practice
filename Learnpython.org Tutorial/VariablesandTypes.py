# Numbers
# myint = 7
# print(myint)

# myfloat = 7.0
# print(myfloat)
# myfloat = float(7)
# print(myfloat)

# Strings, second is better if there are apostrophes
# mystring = 'hello'
# print(mystring)
# mystring = "hello"
# print(mystring)

# Operators
# one = 1
# two = 2
# three = one + two
# print(three)

# hello = "hello"
# world = "world"
# helloworld = hello + " " + world
# print(helloworld)

# Assignments on multiple variables simulatneously
# a, b = 3, 4
# print(a, b)

# CANNOT mix operators between numbers and strings
# one = 1
# two = 2
# hello = "hello"
# print(one + two + hello)

# Exercise: create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
# change this code
mystring = "hello"
myfloat = float(10)
myint = 20
# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)