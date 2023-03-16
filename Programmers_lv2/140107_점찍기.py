import math
def solution(k, d):
    answer = 0

    for i in range(0, d+1, k):
        for j in range(0, d+1, k):
            if math.sqrt(i**2 + j**2) <= d:
                answer += 1
                print(i, j)
    print(answer)
    return answer

solution(1,5)