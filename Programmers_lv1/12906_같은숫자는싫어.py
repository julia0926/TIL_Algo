# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    tmp = []
    for i in range(len(arr)):
        if i == 0:
            tmp.append(arr[i])
        elif arr[i] != arr[i-1]:
            tmp.append(arr[i])
    return tmp

print(solution1([1,1,3,3,0,1,1]))