#https://school.programmers.co.kr/learn/courses/30/lessons/118666
from collections import defaultdict

def solution(survey, choices):
    personal_type = defaultdict(int)

    for s, c in zip(survey, choices):
        if c < 4:
            personal_type[s[0]] += 4 - c
        else:
            personal_type[s[1]] += c - 4
    person_list = [('R','T'), ('C','F'), ('J','M'), ('A','N')]
    answer = ''
    for person in person_list:
        print(personal_type[person[0]],personal_type[person[1]] )
        if personal_type[person[0]] > personal_type[person[1]] or personal_type[person[0]] == personal_type[person[1]]:
            answer += person[0]
        elif personal_type[person[0]] < personal_type[person[1]]:
            answer += person[1] 

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["CF", "FC", "CF"], [7,1,3]))