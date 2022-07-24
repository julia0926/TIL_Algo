# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# ---- 1차 시도  (실패: 시간초과 -> 정확성 26.7%)
from itertools import permutations

def solution(numbers):
    numbers = list(map(str, numbers))
    result = []
    answer = 0
    piv_list = list(map(list,permutations(numbers, len(numbers))))
    for i in piv_list:
        result.append("".join(i))
        answer = max(answer, int("".join(i)) )
    return str(answer)

print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2]))