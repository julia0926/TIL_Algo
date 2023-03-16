# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

import math

def solution(X, Y, D):
    return math.ceil((Y - X) / D)

print(solution(10, 85, 30))