# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    if total == 0 or num == 1:
        return [total]
    value = [k for k in range(1, 101)]
    # print(value)
    idx = 0
    while idx <= 100:
        # print(value[idx:idx+num], sum(value[idx:idx+num]))
        if sum(value[idx:idx+num]) == total:
            return value[idx:idx+num]
        else:
            idx += 1
    

print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(1, 0))
print(solution(1, 135))