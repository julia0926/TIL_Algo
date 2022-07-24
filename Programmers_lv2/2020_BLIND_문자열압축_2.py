# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# 22.07.24 3번째 시도

def solution(s):
    answer = 1001
    #몇개 단위로 압축 -> 해당 압축과 다음 압축을 비교함
    for i in range(1, len(s)//2+1): #1. 몇개 단위로 압축 
        count = 1 #해당 단위가 몇개인지
        result = "" #단위의 문자열 
        start = s[:i] #시작 문자열 
        for j in range(i, len(s)+i, i): #2. 해당 압축과 다음 압축을 비교함 
            if start == s[j:j+i]: #시작과 단위로 자른 문자열이 같으면 
                count += 1
            else: #다르다면
                if count == 1: #문자열이 하나라면 숫자 앞에 붙일 필요 없음
                    result += start
                else: #문자열이 여러개라면 앞에 숫자 붙임,,
                    result += str(count) + start
                count = 1
                start = s[j:j+i]
                print(result)
        answer = min(answer, len(result))
    return answer

print(solution("ababcdcdababcdcd"))
print(solution("a"))