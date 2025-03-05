from Model import *
from View import *

def main():
    while True:
        choice = display_menu()

        if choice == "1":
            x,y = get_numbers()
            res = summ(x,y)
            result(res)
        elif choice == "2":
            x, y = get_numbers()
            res = sub(x,y)
            result(res)
        elif choice == "3":
            x, y = get_numbers()
            res = multiplication(x,y)
            result(res)
        elif choice == "4":
            x, y = get_numbers()
            res = division(x,y)
            result(res)
        elif choice == "5":
            x, y = get_numbers()
            res = integer_division(x,y)
            result(res)
        elif choice == "6":
            x, y = get_numbers()
            res = division_with_remainder(x,y)
            result(res)
        elif choice == "7":
            x, y = get_numbers()
            res = degree(x,y)
            result(res)

        elif choice == "0":
            show_message("Пока!")
            break
        else:
            show_message("Неверный выбор, попробуй снова")


main()
