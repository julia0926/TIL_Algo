# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    mid = total // num
    for i in range(mid - (num-1)//2, mid + (num+2)//2):
        print(i)


print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))