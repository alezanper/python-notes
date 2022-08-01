# Raising an error
def a_number(number):
    if not isinstance(number, (int,float)):
        raise TypeError(number, "must be numeric")
    else:
        print (number, "is a number")

a_number(19)    # 19 is a number
a_number("10a") # error