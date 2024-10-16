def force_number(num, force):
    print(f"Force of number: {num ** force}")

def summ(num_1, num_2):
    print(f"Summ of number: {num_1 + num_2}")

def subtraction(num_1, num_2):
    print(f"Subtraction of number: {num_1 - num_2}")

def multiplication(num_1, num_2):
    print(f"Multiplication of number: {num_1 * num_2}")
def division(num_1, num_2):
    try:
        print(f"Division of number: {num_1 / num_2}")
    except ZeroDivisionError:
        print("You can't divide by zero")


num_1 = int(input("Enter a number 1: "))
num_2 = int(input("Enter a number 2: "))


force_number(num_1, num_2)
summ(num_1, num_2)
subtraction(num_1, num_2)
multiplication(num_1, num_2)
division(num_1, num_2)
