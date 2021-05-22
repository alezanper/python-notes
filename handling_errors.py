"""
Python 3 defines 63 built-in exceptions, and all of them form a tree-shaped hierarchy

ArithmeticError
Location: BaseException ← Exception ← ArithmeticError

AssertionError
Location: BaseException ← Exception ← AssertionError

BaseException
Location: BaseException

IndexError
Location: BaseException ← Exception ← LookupError ← IndexError

KeyboardInterrupt
Location: BaseException ← KeyboardInterrupt

MemoryError
Location: BaseException ← Exception ← MemoryError

LookupError
Location: BaseException ← Exception ← LookupError

OverflowError
Location: BaseException ← Exception ← ArithmeticError ← OverflowError

ImportError
Location: BaseException ← Exception ← StandardError ← ImportError

KeyError
Location: BaseException ← Exception ← LookupError ← KeyError

"""

# try-catch
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")
print("THE END.")

# try-catch tree
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")
print("THE END.")

# assert
x = float(input("Enter a number: "))
assert x >= 0.0