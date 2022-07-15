# https://school.programmers.co.kr/learn/courses/30/lessons/86051?language=python3

def solution(numbers):
    set_numbers = set(numbers)
    set_piv = set([i for i in range(1, 10)])
    #set_piv = set(range(10))
    answer = sum(list(set_piv - set_numbers))
    return answer

print(solution([1,2,3,4,6,7,8,0]))