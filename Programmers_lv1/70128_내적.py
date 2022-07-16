# https://school.programmers.co.kr/learn/courses/30/lessons/70128?language=python3

def solution(a, b):
    #내코드 
    answer = []
    for x, y in zip(a, b):
        answer.append(x*y)
    return sum(answer)

    #한줄로 푼 코드 (내 코드 요약본인듯)
    #return sum([x * y for x, y in zip(a,b)])
    
print(solution([1,2,3,4], [-3,-1,0,2]))