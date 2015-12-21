import random


# Heap sort
# złożoność czasowa wynosi  O(n\log n), a pamięciowa –  O(n)
# Algorytm sortowania przez kopcowanie składa się z dwóch faz.
# W pierwszej sortowane elementy reorganizowane są w celu utworzenia kopca. W drugiej zaś dokonywane jest właściwe sortowanie.

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def down(list_to_sort, node, size_var):
    left = int(2 * node + 1)
    right = int(2 * node + 2)
    largest = node
    if left <= size_var - 1 and list_to_sort[left] > list_to_sort[node]:
        largest = left
    if right <= size_var - 1 and list_to_sort[right] > list_to_sort[largest]:
        largest = right
    if largest != node:
        swap(list_to_sort, node, largest)
        down(list_to_sort, largest, size_var)


def create_heap(list_to_sort, size_var):
    p = (size_var / 2) - 1
    while p >= 0:
        down(list_to_sort, p, size_var)
        p -= 1


def sort(list_to_sort):
    size = len(list_to_sort)
    create_heap(list_to_sort, size)
    end = size - 1
    while end > 0:
        swap(list_to_sort, 0, end)
        down(list_to_sort, 0, end)
        end -= 1
    return list_to_sort
