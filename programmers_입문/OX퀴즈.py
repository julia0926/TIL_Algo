# https://school.programmers.co.kr/learn/courses/30/lessons/120907

def solution(quiz):
    answer = []
    for q in quiz:
        dq = q.split('=')
        op = eval(dq[0])
        result = int(dq[1])
        if op == result:
            answer.append("O")
        else:
            answer.append("X")
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))