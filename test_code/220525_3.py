from bisect import bisect_left, bisect_right
from itertools import combinations
from typing import Counter


def solution(arr):
    max_value = Counter(arr).most_common(1)[0][0]
    start_index = bisect_left(arr, max_value)
    end_index = bisect_right(arr, max_value)
    return sum(arr[start_index:end_index])


print(solution([1,3,6,1,6,6,9,9]))

print(list(combinations([1,2,3,4], 3)))