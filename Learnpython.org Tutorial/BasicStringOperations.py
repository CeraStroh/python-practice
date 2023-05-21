# Prints 12, including punctuation and spaces
# astring = "Hello world!"
# print(len(astring))

# Prints 4
# astring = "Hello world!"
# print(astring.index("o"))

# Prints 3, counts number of l's in string
# astring = "Hello world!"
# print(astring.count("l"))

# Prints "lo w" (can use negative numbers to start from end, -3 is 3rd character from end)
# astring = "Hello world!"
# print(astring[3:7])

# Prints l, [start:stop:step]
# astring = "Hello world!"
# print(astring[3:7:2])

# Both print "lo w"
# astring = "Hello world!"
# print(astring[3:7])
# print(astring[3:7:1])

# Prints it backwards
# astring = "Hello world!"
# print(astring[::-1])

# Print it in all uppercase and all lowercase
# astring = "Hello world!"
# print(astring.upper())
# print(astring.lower())

# First is "True", second is "False"
# astring = "Hello world!"
# print(astring.startswith("Hello"))
# print(astring.endswith("asdfasdfasdf"))

# Splits string into a bunch of strings grouped together in a list. First item is "Hello" and second will be "world!"
# astring = "Hello world!"
# afewwords = astring.split(" ")

# Exercise: Print out the correct information by changing the string.s = "Hey there! what should this string be?"
s = "Hey there! what shou"
# Length should be 20
print("Length of s = %d" % len(s))
# First occurrence of "a" should be at index 8
s = "Hey therae! what should this string be?"
print("The first occurrence of the letter a = %d" % s.index("a"))
# Number of a's should be 2
s = "Hey there!a what should this string be?"
print("a occurs %d times" % s.count("a"))
# Slicing the string into bits
s = "Hey there! what should this string be?"
print("The first five characters are '%s'" % s[:5]) # Start to 5
s = "Hey there! what should this string be?"
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
s = "Hey there! what should this string be?"
print("The thirteenth character is '%s'" % s[12]) # Just number 12
s = "Hey there! what should this string be?"
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
s = "Hey there! what should this string be?"
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
# Convert everything to uppercase
s = "HEY THERE! WHAT SHOULD THIS STRING BE?"
print("String in uppercase: %s" % s.upper())
# Convert everything to lowercase
s = "hey there! what should this string be?"
print("String in lowercase: %s" % s.lower())
# Check how a string starts
s = "StrHey there! what should this string be?"
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
# Check how a string ends
s = "Hey there! what should this string be?ome"
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
# Split the string into three separate strings, each containing only a word
s = "Hey there! what"
print("Split the words of the string: %s" % s.split(" "))