# Завдання 1
# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.
# Завдання 2
# Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.
# Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
# Завдання 4
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.
# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
# Завдання 6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.


def task_one(num_list):
    print("Завдання 1")
    num_summ = sum(num_list)
    print(num_summ)


def task_two(num_list):
    print("Завдання 2")
    min_numm = min(num_list)
    print(min_numm)


def task_three(num_list):
    print("Завдання 3")
    all_simple = 0
    for num in num_list:
        dev_count = 0
        i = 1
        while i < num:
            if num % i == 0:
                dev_count += 1
            i += 1
        if dev_count <= 1 and num != 0:
            all_simple += 1
    print(f"Количество простых чисел {all_simple}")


def task_four(num_list):
    print("Завдання 4")
    set_number = int(input("Pls input number your want to delete: "))
    del_counts = 0
    int_to_del = []
    for num in num_list:
        index = 0
        if num == set_number:
            del_counts += 1
            int_to_del.append(num)
        index += 1
    for x in int_to_del:
        while x in num_list:
            num_list.remove(x)

    print(f"This function deleted {set_number} in your list {del_counts} times")
    print(f"Now your list looks like: {num_list}")


def task_five(num_list1, num_list2):
    print("Завдання 5")
    num_list_all = num_list1 + num_list2
    print(num_list_all)


def task_six(num_list):
    print("Завдання 6")
    pov_num = int(input("Pls input multiplication degree: "))
    i = 0
    for num in num_list:
        num_list[i] = pow(num, pov_num)
        i += 1
    print(num_list)


try:

    print("Pls input 2 lists of integer using space.")

    numbers_1 = list(map(int, input("List 1: ").split()))
    numbers_2 = list(map(int, input("List 2: ").split()))

    task_one(numbers_1)
    task_two(numbers_1)
    task_three(numbers_1)
    task_four(numbers_1)
    task_five(numbers_1, numbers_2)
    task_six(numbers_1)

except ValueError as e:
    print("Pls input integer")
except Exception as e:
    print(e)
