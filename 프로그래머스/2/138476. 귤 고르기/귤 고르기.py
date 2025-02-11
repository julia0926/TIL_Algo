from collections import Counter

def solution(k, tangerine):
    answer = 0
    couter = Counter(tangerine)

    sorted_val = sorted(couter.values(), reverse=True)
    for val in sorted_val:
        if k <= 0:
            break
        k -= val
        answer += 1
    return answer