# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

def solution(A):
    cnt = len(A)+1
    arr = set(i for i in range(1, cnt+1))
    return list(arr - set(A))[0]