# https://school.programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    result = []
    start = s[2:-2]
    start = start.split("},{")
    # 이렇게 한줄로도 위의 두줄 커버 -> 왼쪽 { 제거 오른쪽 } 제거
    #start = s.lstrip("{").rstrip("}").split("},{")
    for i in start:
        answer.append(list(map(int, i.split(","))))
    answer = sorted(answer,key=len)
    for i in answer:
        for j in i:
            if j not in result:
                result.append(j)
    return result

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))