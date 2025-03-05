
def summ(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    if y != 0:
        print("На 0 делить нельзя!")
    else:
        return x/y

def division_with_remainder(x,y):
    if y != 0:
        print("На 0 делить нельзя!")
    else:
        return x%y

def integer_division(x,y):
    if y != 0:
        print("На 0 делить нельзя!")
    else:
        return x//y


def degree(x,y):
    return x**y
