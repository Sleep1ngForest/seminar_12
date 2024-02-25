from logger import input_data, print_data


def interface():
    print ("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n 1 - запись данных \n 2 - вывод данных")
command = int(input('Введите число '))

while command !=1 and command != 2:
    print("Неправильный ввод")
    command = int(input('Введите число '))

if command == 1:
    input_data()
elif command == 2:
    print_data()

def check_number(n):
    while n < 1 or n > 5:
        n = int(input("Ошибка, такого номера команды не "
                      "существует! Введите цифру от 1 до 5\n"
                      "Выберите функцию:\n"
                      "1. Добавить\n"
                      "2. Удалить\n"
                      "3. Изменить\n"
                      "4. Вывод\n"
                      "5. Выход\n"
                      "Введите номер команды: "))
    return n


def start_menu():
    command = None
    while command != 5:
        command = int(input("Доброго времени суток!\n"
                            "Выберите функцию:\n"
                            "1. Добавить\n"
                            "2. Удалить\n"
                            "3. Изменить\n"
                            "4. Вывод\n"
                            "5. Выход\n"
                            "Введите номер команды: "))
        command = check_number(command)
        if command == 1:
            add_row()
        elif command == 2:
            delete_row()
        elif command == 3:
            change_row()
        elif command == 4:
            print_file()
    print("Спасибо, что воспользовались нашими услугами!\n"
          "Всего доброго! Приходите к нам ещё :)")    
    print_data()