# https://school.programmers.co.kr/learn/courses/30/lessons/43163

#결과 : 최소 몇단계의 과정을 거쳐 변환되는지 
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    dq = deque()
    dq.append([begin, 0]) #시작 문자, 변환카운트

    while dq:
        piv_word, count = dq.popleft()
        if piv_word == target:
            return count
        for word in words:
            diff = 0 #문자마다 차이를 확인해야하므로

            for j in range(len(piv_word)): #기준 단어를 하나씩 비교한다
                if word[j] != piv_word[j]: #다를때 하나씩 변환 가능하므로
                    diff += 1
            if diff == 1: #하나 차이나는 words의 word라면
                dq.append([word, count+1])

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))