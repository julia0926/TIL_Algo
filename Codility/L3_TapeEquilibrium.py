# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# 2차시도 dp(buttom-up)로 해결
def solution(A):
    if len(A) == 2:
        return abs(A[0] - A[1])
    tmp = [0] * (len(A)-1)
    tmp[0] = A[0]
    result = []
    sum_v = sum(A)
    for i in range(len(A)-1): #1~5
        if i == 0:
            tmp[i] = A[i]
        tmp[i] = tmp[i-1] + A[i]
        result.append(abs(tmp[i] - (sum_v - tmp[i])))
        #print(sum_v - tmp[i])
    return min(result)