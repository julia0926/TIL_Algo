#https://programmers.co.kr/learn/courses/30/lessons/42746
#functools 공식문서 : https://docs.python.org/ko/3/howto/sorting.html
import functools

def compare(a, b):
    t1 = a+b #610
    t2 = b+a #106
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #t1이 크면 1, t2가 크면 -1, 같으면 0

def solution(numbers):
    arr = list(map(str, numbers))
    arr = sorted(arr, key=functools.cmp_to_key(compare), reverse=True)
    return str(int(''.join(arr))) #0000일때 0으로 리턴 

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))