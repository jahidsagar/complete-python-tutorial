# -------- part 1: escape sequences
print("My name is \"John\".") # Using double quotes to escape
print('My name is "John".') # Using single quotes to escape
print("My name is 'John'.") # Using double quotes to escape single quotes
print('My name is \'John\'.') # Using single quotes to escape single quotes
print("My name is \\John\\.") # Using double backslashes to escape

# -------- part 2: type casting
x = input("Enter a number: ")
y = int(x)  # Convert string input to integer
print(type(y))  # Print the type of y
z = float(x)  # Convert string input to float
print(type(z))  # Print the type of z

# -------- part 3: Falsy values
print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # False
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False
print(bool(1))  # True
print(bool("Hello"))  # True

