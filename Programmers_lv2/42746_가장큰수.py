# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 참고 해결 

from functools import cmp_to_key

def compare(a, b):
    val1 = int(a + b)
    val2 = int(b + a)
    return (val1 > val2) - (val2 > val1) #val1이 크면 1, val2가 크면 -1, 같으면 0


def solution(numbers):
    num_to_str = list(map(str, numbers))
    n = sorted(num_to_str, key=cmp_to_key(compare), reverse=True)
    answer = ''.join(n)
    return str(int(answer))
    
print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2]))

'''
정렬 기준이
3034(30, 34) < 3430(34, 30) 문자열 길이 같으면 큰 값이 먼저 
330(3, 30) > 303(30, 3) 문자열 짧은게 먼저 

343 (34, 3) > 334 (3, 34) 
같으면 상관 없는데 333(33, 3) (3, 33)
313(31,3 ) < 331(3,31)
'''