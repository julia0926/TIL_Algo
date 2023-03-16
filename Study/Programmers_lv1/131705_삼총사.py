from itertools import combinations

def solution(number):
    answer = 0

    for v in list(combinations(number, 3)):
        if sum(v) == 0: 
            answer += 1
    return answer

solution([-2, 3, 0, 2, -5])