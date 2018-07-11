# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.


Fruits = ['Хурма', 'Киви', 'Арбуз', 'Яблоко', 'Груша', 'Персик', 'Апельсин']
order = len(Fruits)
for i in range(order):
    print(str(i + 1) + ' ' + '{}'.format(Fruits[i]))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

first_list = [1, 2, 'Ivan', 989, 'hello', 3]
second_list = [4, 7, 989, 'world', 3, 65, 1]
for item in second_list:
    if item in first_list:
        first_list.remove(item)
print(first_list)
print(second_list)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


list_of_numbers = [3, 34, 78, 4, 1, 8, 120, 99]
new_list = []
for number in list_of_numbers:
    if number % 2 > 0:
        new_list.append(number * 2)
    else:
        new_list.append(number / 4)
print(new_list)


