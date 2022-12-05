# https://school.programmers.co.kr/learn/courses/30/lessons/140108

'''
문제를 잘못 이해하고, 문자열 각각의 개수를 세는줄 알았다.
처음 문자열 / 그외 문자열의 개수를 비교하는 문제였음
'''


def solution(s):
    first = 0
    diff = 0
    piv = s[0]
    answer = 0

    for i in range(len(s)):
        if piv == s[i]:
            first += 1
        else:
            diff += 1
        
        if first == diff and first != 0:
            answer += 1
            
            if i + 1 < len(s):
                piv = s[i+1]
            first, diff = 0, 0

    if first != 0:
        answer += 1

        

    
    return answer

solution("abracadabra")
solution("aaabbaccccabba")