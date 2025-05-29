# part 1: comment
"""
This is a comment, in python comments start with a hash symbol. there is no multi-line comment syntax in python, 
but you can use triple quotes to create a multi-line string that acts like a comment.
"""

# part 2: print

print('Hello World!') # single quotes
print("Hello World!") # double quotes
print('''Hello World!''') # triple single quotes
print("""Hello World!""") # triple double quotes
print('hello', 'world') # multiple arguments, separated by commas, this will print with a space in between
print('hello' + 'world') # concatenation, this will print without a space in between
print('hello', 'world', sep='-') # custom separator, this will print with a hyphen in between
print('hello', 'world', end='!') # custom end, this will print with an exclamation mark at the end
print('hello', 'world', sep='-', end='!') # custom separator and end, this will print with a hyphen in between and an exclamation mark at the end
print() # print a new line

# part 3: input
a =  input("Enter your name: ")
print('your name is: ',a)

# part 4: print types
print(type('hello')) # <class 'str'>
print(type(1)) # <class 'int'>
print(type(1.0)) # <class 'float'>
print(type(True)) # <class 'bool'>
print(type(None)) # <class 'NoneType'>
print(type([1, 2, 3])) # <class 'list'>
print(type((1, 2, 3))) # <class 'tuple'>
print(type({1, 2, 3})) # <class 'set'>
print(type({'a': 1, 'b': 2})) # <class 'dict'>
print(type(a))


# part 4: Python Implementation
# CPython: The default implementation of Python, written in C.
# PyPy: An alternative implementation of Python, written in RPython, which is a subset of Python.
# IronPython: An implementation of Python for the .NET framework.
# Jython: An implementation of Python for the Java platform.

# PEP: Python Enhancement Proposal