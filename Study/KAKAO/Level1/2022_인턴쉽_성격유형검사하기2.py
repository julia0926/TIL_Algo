#https://school.programmers.co.kr/learn/courses/30/lessons/118666
from collections import defaultdict

def solution(survey, choices):
    person_list = [('R', 'T'), ('C','F'), ('J','M'),('A','N')]
    score_dic = defaultdict(int)
    for sort, choice in zip(survey, choices):
        if choice < 4:
            score_dic[sort[0]] += 4-choice
        elif choice > 4:
            score_dic[sort[1]] += choice-4
    answer = ''
    for a, b in person_list:
        if score_dic[a] >= score_dic[b]: #동점이거나 앞성격유형이 더 크면 
            answer += a
        else:
            answer += b

    return answer


solution(["AN", "CF", "MJ", "RT", "NA"]	, [5, 3, 2, 7, 5]	)