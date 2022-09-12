# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i < j: 
                new_arr[i][j] = new_arr[i][j-1] + 1
                continue
            new_arr[i][j] = i+1
    new_arr = sum(new_arr, [])
    return new_arr[left:right+1]

print(solution(3,2,5))
solution(4,7,14)