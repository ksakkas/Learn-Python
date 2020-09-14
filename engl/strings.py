# Python Strings

x = '''The aim of the department is to promote information science, 
computer systems and telecommunications, as well as their applications. 
The Department has modern facilities on the campus of the historic city of Arta.'''
print(x)
print("-----------------------------------------------------------")

y = "Hello World!"
print(y[0])     # Get the characters from position 0
print(y[6:11])  # Get the characters from position 6 to position 11
print("-----------------------------------------------------------")

print(len(y))   # Returns the length of a string

k = "  DIT"
m = "dit"
print(k.strip())    # Removes any whitespace from the beginning or the end
print("----------------------------------------------------------")

print(k.lower())    # Returns the string in lower case
print("----------------------------------------------------------")

print(m.upper())    # Returns the string in upper case
print("----------------------------------------------------------")

l="Tit"
print(l.replace("T", "D"))  # Replaces a string with another string
print("----------------------------------------------------------")

q="DIT - UOI"
print(q.split("-"))
print("----------------------------------------------------------")

a = "DIT"
b = "I" in a    # Check if the phrase "I" is present in the following text
print(b)
print("----------------------------------------------------------")

b = "o" not in a    # Check if the phrase "I" is NOT present in the following text
print(b)
print("----------------------------------------------------------")

a = "Hello"
b = "World"
c = a + b   # Merge variable a with variable b into variable c
print(c)

c = a + "   " + b
print(c)

age = 21
txt = "My name is Kostas, and I am {}"
print(txt.format(age))  # The format() method takes the passed arguments, formats them, 
                        # and places them in the string where the placeholders {} are:

kr = "DIT--\"UOI\"."    # The escape character allows you to use double quotes 
                        # when you normally would not be allowed:
print(kr)



