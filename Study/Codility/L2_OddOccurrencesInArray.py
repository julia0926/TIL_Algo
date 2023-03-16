# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

from collections import Counter

def solution(A):
    # write your code in Python 3.6
    counter = Counter(A)
    for key, value in counter.items():
        if value % 2 != 0:
            return key
print(solution([9, 3, 9, 3, 9, 7, 9]))