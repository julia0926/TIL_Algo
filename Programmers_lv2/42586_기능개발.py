# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3
# 시간복잡도 : O^2
# 개선 : O로 고쳐보자,, (정답이긴 함)
def solution(progresses, speeds):
    days = []
    for idx, progress in enumerate(progresses):
        finish_day = (100 - progress) // speeds[idx]
        if progress + (finish_day * speeds[idx]) < 100:
            finish_day += 1
        days.append(finish_day)

    answer = []
    cnt = 1
    first = days[0]
    for i in range(1, len(days)):
        if first < days[i]:
            answer.append(cnt)
            first = days[i]
            cnt = 0
        cnt += 1
    answer.append(cnt)
    return answer
        

print(solution([93, 30, 55], [1, 30, 5]))