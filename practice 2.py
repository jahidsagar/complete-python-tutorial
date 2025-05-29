# ------------ part 1: String Slicing in Python
course = "This is a Python course"

print(course)

print(course[0])  # First character
print(course[-1])  # Last character

print(course[0:5])  # First five characters
print(course[:5])  # First five characters (alternative syntax)

print(course[0:])  # From the start to the end
print(course[::])  # Full string (no slicing)

# using step in slicing
print(course[0:20:2])  # Every second character from the first 20 characters

# reversing the string
print(course[::-1])  # Reversed string

# slicing with negative indices
print(course[-6:])  # Last six characters


# ------------ part 2: String Methods in Python
print(course.upper())  # Convert to uppercase
print(course.lower())  # Convert to lowercase
print(course.title())  # Convert to title case
print(course.find('Python'))  # Find the index of a substring
print(course.replace('Python', 'Java'))  # Replace a substring
print('Python' in course)  # Check if a substring exists
print('Java' not in course)  # Check if a substring does not exist

# ------------ part 3: String concatenation
greeting = "Hello"
name = "World"
full_greeting = greeting + " " + name  # Concatenation with space
print(full_greeting)  # Output: Hello World

# ------------ part 4: String Formatting and Manipulation
# String formatting
age = 30
formatted_string = f"{greeting}, {name}! You are {age} years old."  # f-string formatting
print(formatted_string)  # Output: Hello, World! You are 30 years old.
# String interpolation
formatted_string2 = "Hello, {}! You are {} years old.".format(name, age)  # Using format method
print(formatted_string2)  # Output: Hello, World! You are 30 years old.

# ------------ part 5: String splitting and joining
sentence = "This is a Python course"
words = sentence.split()  # Split into words, default separator is whitespace
print(words)  # Output: ['This', 'is', 'a', 'Python', 'course']

joined_sentence = " ".join(words)  # Join words with space
print(joined_sentence)  # Output: This is a Python course

# ------------ part 6: String stripping 
whitespace_string = "   Hello World!   "
stripped_string = whitespace_string.strip()  # Remove leading and trailing whitespace
print(stripped_string)  # Output: Hello World!

space_left = "   Hello World!"
space_right = "Hello World!   "
left_stripped = space_left.lstrip()  # Remove leading whitespace
right_stripped = space_right.rstrip()  # Remove trailing whitespace
print(left_stripped)  # Output: Hello World!
print(right_stripped)  # Output: Hello World!


# ------------ part 7: String checking 
# String checking
print(course.startswith("This"))  # Check if the string starts with a substring
print(course.endswith("course"))  # Check if the string ends with a substring

# ------------ part 8: String comparison
print("Python" == "Python")  # Check if two strings are equal
print("Python" != "Java")  # Check if two strings are not equal
print("Python" < "Java")  # Compare strings lexicographically
print("Python" == "python")  # Case-sensitive comparison

# ------------ part 9: String iteration
for char in course:
    print(char, end=' ')  # Print each character in the string with a space

# Iterating through the string using index
print()
for i in range(len(course)):
    print(course[i], end=' ')  # Print each character using index

# iterating through the string with enumerate
print()
for i,c in enumerate(course):
    print(f"Index: {i}, Character: {c}")  # Print index and character
