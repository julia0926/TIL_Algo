def solution(N, stages):
    fail_rate = {}
    
    total = len(stages)
    for stage_num in range(1, N+1):
        if total != 0:
            count = stages.count(stage_num)
            fail_rate[stage_num] = count / total #실패율 저장
            total -= count
        else:
            fail_rate[stage_num] = 0
        
        # print(f'{cnt} / {total} = {cnt / total}')
    result = dict(sorted(fail_rate.items(), key=lambda x: x[1], reverse=True)) #딕셔너리 value 내림차순
    return [*result]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))