from collections import Counter

def solution(common):
    diff = []
    for i in range(2):
        diff.append(common[i+1] - common[i])
    
    if len(Counter(diff).keys()) == 1:
        return max(common) + diff[0]
    else:
        
        t = diff[1] // diff[0]
        return max(common) * t


# solution([1, 2, 3, 4]	)
# solution([2, 4, 8])
print(solution([1,2,4]))