from itertools import combinations

def solution(nums):
    combi = set(combinations(nums,len(nums)//2))
    answer = 0
    for c in combi:
        tmp = []
        count = 0
        for j in c:
            if j not in tmp:
                tmp.append(j)
                count += 1
        answer = max(answer, count)
    return answer

# solution([3,1,2,3])
solution([3,3,3,2,2,2]	)