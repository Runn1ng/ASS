#Задание 1
d = {}
def psp(n: int) -> str:
    def get_gen(k):
        if k not in d:
            d[k] = psp(k)
        return d[k]

    if n <= 0:
        return set([''])

    new_data = set()
    for i in get_gen(n - 1):
        new_data.add('(' + i + ')')
        new_data.add(i + '()')
        new_data.add('()' + i)

    for j in range(2, n // 2 + 1):
        b = get_gen(j)
        for i in get_gen(n - j):
            for k in b:
                new_data.add(i + k)
                new_data.add(k + i)

    new_data = '\n'.join(sorted(new_data))
    return new_data

#Задание 2
import functools
from typing import List
def my_sort(left: tuple, right: tuple):
    return -1 if (left[0] * 10 ** len(right[1]) + right[0]) > (right[0] * 10 ** len(left[1]) + left[0]) else 1

def largest_number(numbers: List[int]) -> str:
    numbers.sort(key=functools.cmp_to_key(my_sort))
    result_number = ''.join([x[1] for x in numbers])
    return result_number

# задание 1
# print(psp(int(input())), end='')
# задание 2
input() # выкидываем n, т.к. оно не нужно
numbers = [tuple([int(x), x]) for x in input().split(' ')]
print(largest_number(numbers), end='')
