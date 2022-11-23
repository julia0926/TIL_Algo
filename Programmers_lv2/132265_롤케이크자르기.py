#1번째 시도, 실패
def solution1(topping):
    answer = 0
    for i in range(1, len(topping)):
        a, b = len(set(topping[:i])), len(set(topping[i:]))
        if a == b:
            answer += 1

    return answer

# 투포인터 공부 후 재시도해야됨
from collections import Counter
def solution(topping):
    answer = 0
    left, counter = [], []
    end = 0
    for i in range(len(topping)):
        if topping[i] not in left:
            left.append(topping[i])
        print(left)

    return answer

solution([1, 2, 1, 3, 1, 4, 1, 2]	)