from typing import List

# Задание 1
def nearest_zero(array: List[int]) -> List[int]:
    distance = [0] * len(array)
    distance_zero = float('inf')
    for i, value in enumerate(array):
        if value == 0:
            distance[i] = 0
            distance_zero = 0
            for j in range(i, 0-1, -1):
                if distance_zero <= distance[j]:
                    distance[j] = distance_zero
                    distance_zero += 1
                else:
                    break
            distance_zero = 0
        else:
            distance_zero += 1
            distance[i] = distance_zero
    return distance


street = [int(house) for house in input().split()]
print(*nearest_zero(street))


# Задание 2
def sleight_of_hand(k: int) -> int:
    points = 0
    counter = [0] * 10
    for row in range(4):
        for value in input():
            if value != '.':
                counter[int(value)] += 1
    for value in counter:
        points += 1 if 0 < value <= 2 * k else 0
    return points

finger_count = int(input())
print(sleight_of_hand(finger_count))