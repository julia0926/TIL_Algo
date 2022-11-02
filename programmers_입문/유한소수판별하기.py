def solution(a, b):
    for i in range(min(a,b), 0, -1):
        if a%i == 0 and b % i == 0:
            b //= i
            break
    #소인수 분해
    idx = 2
    arr = []
    while idx <= b:
        if b % idx == 0:
            arr.append(idx)
            b /= idx
        else:
            idx += 1
    #2와 5만 존재해야함
    for i in arr:
        if i != 2 and i != 5:
            return 2
    return 1

# print(solution(7, 20))
print(solution(12, 36))