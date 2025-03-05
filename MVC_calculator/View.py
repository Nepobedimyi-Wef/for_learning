def display_menu():
    print("\nВыбери действие: 1 - сложить, 2 - вычесть, 3 - умножить, 4 - деление, 5 - целочисленное деление, 6 - остаток от деления, 7 - степень, 0 - выход")
    choice = input("Введи номер действия: ")
    return choice


def get_numbers():
    print("Введите 1 число: ")
    x = int(input())
    print("Введите 2 число: ")
    y = int(input())
    return x, y


def result(res):
    print("Результат:",res)

def show_message(message):
    print(message)
