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

## Exception additional comments
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n
print(reciprocal(2))    #Everything went fine   0.5
print(reciprocal(0))    #Division failed        None

## Finally
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n

print(reciprocal(2))    #Everything went fine   It's time to say good bye   0.5
print(reciprocal(0))    #Division failed        It's time to say good bye   None

## Exceptions are classes
try:
    i = int("Hello!")
except Exception as e:
    print(e)            #invalid literal for int() with base 10: 'Hello!'

##Print exception tree function
def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")
    print(thisclass.__name__)
    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)

print_exception_tree(BaseException)

## Create my own exception
class MyZeroDivisionError(ZeroDivisionError):	
    pass

def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:		
        raise ZeroDivisionError("some bad news")

for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')

# Division by zero
# Division by zero
# Original division by zero
# My division by zero

##My own exception example
class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)