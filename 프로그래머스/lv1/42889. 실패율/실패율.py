#실패율이 높은 ~ , 내림차순으로 
from bisect import bisect_left,bisect_right
def solution(N, stages):
    result = []
    stages.sort()
    total = len(stages)
    diff_arr = []
    for i in range(1, N+1):
        idx = bisect_left(stages,i)
        idx2 = bisect_right(stages,i)
        diff = idx2 - idx
        if diff == 0:
            diff_arr.append(0)
        else:
            diff_arr.append(diff/total)
        total -= diff
    dic = {}
    for i, v in enumerate(diff_arr):
        dic[i+1] = v
    result = sorted(dic.items(), key=lambda x: -x[1])
    answer = []
    # print(result)
    for a, _ in result:
        answer.append(a)
    # print(answer)
    return answer