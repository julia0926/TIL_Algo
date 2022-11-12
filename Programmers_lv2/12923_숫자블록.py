#실패!!
#https://school.programmers.co.kr/learn/courses/30/lessons/12923
def solution(begin, end):
    arr = [0] * (end+1)
    
    for i in range(begin, end//2+1):
        start = i * 2
        while start <= end:
            arr[start] = i
            start += i
    return arr[1:]



solution(1, 10)