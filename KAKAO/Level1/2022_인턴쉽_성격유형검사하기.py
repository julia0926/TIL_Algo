#https://school.programmers.co.kr/learn/courses/30/lessons/118666
from collections import defaultdict

def solution(survey, choices):
    result = defaultdict(int)
    person_list = [('R','T'), ('C','F'), ('J','M'), ('A','N')]
    for s, c in zip(survey, choices):
        if c < 4:
            result[s[0]] += 4 - c
        else:
            result[s[1]] += c - 4
    answer = ""
    for person in person_list:
        if result[person[0]] >= result[person[1]]:
            answer += person[0]
        else:
            answer += person[1]
    return answer

# print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["CF", "FC", "CF"], [7,1,3]))