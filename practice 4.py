# ---------- part 1: arithmatic operations 
a, b = 4,2
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation

# ---------- part 2: Assignment operators
x, y = 5, 10
print("x += y:", x + y)  # Add and assign
print("x -= y:", x - y)  # Subtract and assign
print("x *= y:", x * y)  # Multiply and assign
print("x /= y:", x / y)  # Divide and assign
print("x //= y:", x // y)  # Floor divide and assign
print("x %= y:", x % y)  # Modulus and assign
print("x **= y:", x ** y)  # Exponentiate and assign
print("x &= y:", x & y)  # Bitwise AND and assign
print("x |= y:", x | y)  # Bitwise OR and assign
print("x ^= y:", x ^ y)  # Bitwise XOR and assign
print("x >>= y:", x >> y)  # Bitwise right shift and assign
print("x <<= y:", x << y)  # Bitwise left shift and assign
print(c := 15) # Assignment expression (walrus operator)
print(c)

# ---------- part 3: Comparison operators
a, b = 10, 20
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater than or equal to
print("a <= b:", a <= b)  # Less than or equal to

# ---------- part 4: Logical operators
print("True and False:", True and False)  # Logical AND
print("True or False:", True or False)    # Logical OR
print("not True:", not True)                # Logical NOT

# ---------- part 5: Identity operators
x = [1, 2, 3]
y = x
z = x[:]
print("x is y:", x is y)  # Identity (same object)
print("x is not z:", x is not z)  # Not identity (different object)
print("x == z:", x == z)  # Equality (same content)

# ---------- part 6: Membership operators
my_list = [1, 2, 3, 4, 5]
print("2 in my_list:", 2 in my_list)  # Membership (element exists)
print("6 not in my_list:", 6 not in my_list)  # Non-membership (element does not exist)

# ---------- part 7: Bitwise operators
a, b = 5, 3
print("a & b:", a & b)  # Bitwise AND
print("a | b:", a | b)  # Bitwise OR
print("a ^ b:", a ^ b)  # Bitwise XOR
print("~a:", ~a)        # Bitwise NOT
print("a << 1:", a << 1)  # Bitwise left shift
print("a >> 1:", a >> 1)  # Bitwise right shift