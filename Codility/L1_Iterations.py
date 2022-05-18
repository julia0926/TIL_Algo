# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/start/
def solution(N):
    b = bin(N)[2:] #2진수 변환 
    first = b[0]
    count = 0
    result = []
    for i in range(1, len(b)):
        if first != b[i]:
            count += 1
        else:
            result.append(count)
            count = 0
        
    if result == []:
        return 0
    else:
        return max(result)

print(solution(1041))