__author__ = 'Bartek'


def reverse(list_to_reverse, left, right):
    sub_list = list_to_reverse[left - 1:right]
    counter = len(sub_list) - 1
    for i in range(left-1, right):
        list_to_reverse[i] = sub_list[counter]
        counter -= 1
    return list_to_reverse


listExample = [1, 2, 3, 4, 5, 6, 7, 8]
print(reverse(listExample, 2, 4))
# [1, 4, 3, 2, 5, 6, 7, 8]


def reverse_recursive(list_to_reverse, left, right):
    if left < right:
        temporary_variable = list_to_reverse[left-1]
        list_to_reverse[left-1] = list_to_reverse[right-1]
        list_to_reverse[right-1] = temporary_variable
        reverse_recursive(list_to_reverse, left+1, right-1)
    return list_to_reverse

listExample = [1, 2, 3, 4, 5, 6, 7, 8]
print(reverse_recursive(listExample, 2, 4))
# [1, 4, 3, 2, 5, 6, 7, 8]

