from itertools import product


def find_twelve(num_list1, num_list2, num_list3):
    """Находит все комбинации чисел из трех списков,
    в сумме дающие 12"""

    for num1 in num_list1:
        for num2 in num_list2:
            for num3 in num_list3:
                if num1 + num2 + num3 == 12:
                    return num1, num2, num3


def find_twelve2(num_list1, num_list2, num_list3):
    for n1, n2, n3 in product(num_list1, num_list2, num_list3):
        if n1 + n2 + n3 == 12:
            return n1, n2, n3


num_list1 = [2, 3, 4, 3]
num_list2 = [5, 5, 10, 2]
num_list3 = [6, 4, 11, 3]


print(find_twelve(num_list1, num_list2, num_list3))
print(find_twelve2(num_list1, num_list2, num_list3))
