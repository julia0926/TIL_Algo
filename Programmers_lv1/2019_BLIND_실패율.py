# https://school.programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    dojun = len(stages)
    fail_rate = {id: 0 for id in range(1, N+1)}
    for now_stage in range(1,N+1):
        if dojun != 0:
            count = stages.count(now_stage)
            fail_rate[now_stage] = count / dojun
            dojun -= count
        else:
            fail_rate[now_stage] = 0

            #딕셔너리의 value 값으로 정렬하고 그냥 failrate를 넘겨줬으므로 keys 값만 들어감 
    answer = sorted(fail_rate, key=lambda x: fail_rate[x], reverse=True)
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
