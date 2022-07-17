#https://school.programmers.co.kr/learn/courses/4008/lessons/13328
def solution(mylist):
    return list(map(int, mylist))

solution(['1', '100', '33'])

#https://school.programmers.co.kr/learn/courses/4008/lessons/13252

def solution(mylist):
    return list(map(len, mylist)) #문자열의 길이만큼 리턴됨