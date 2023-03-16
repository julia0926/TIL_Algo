from collections import Counter

#1번째 시도 
#그냥 슬라이싱 해서 set 길이 비교해서 계산했더니 슬라이싱 비용 많이듬 → 시간초과
def solution1(topping):
    answer = 0
    for i in range(1, len(topping)):
        a, b = len(set(topping[:i])), len(set(topping[i:]))
        if a == b:
            answer += 1

    return answer

def solution(topping):
    set_t = set()
    total = Counter(topping)
    answer = 0

    for t in topping:
        set_t.add(t)
        total[t] -= 1
        if total[t] == 0:
            del total[t]
        if len(set_t) == len(total):
            answer += 1
    return answer 

solution([1, 2, 1, 3, 1, 4, 1, 2]	)