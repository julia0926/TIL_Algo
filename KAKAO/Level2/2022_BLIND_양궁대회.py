def score_calculate(info):
    for idx, value in enumerate(info):
        score = 10 - idx
        if value == 0: continue
        #어피치가 점수 땄을 때 vs 라이언 일 때 비교 
        elif 

def solution(n, info):
    answer = []
    lion_arror = 0
    if n == 1 and sum(info) == 10: return [-1]
    appeach_score, lion_score = 0, 0
    #일단 무조검 큰거부텉 맞추는거 ?! 0점부터 
    while dq:
        



    return answer


# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))