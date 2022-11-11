def solution(citations):
    citations.sort()

    for i in range(len(citations)):
        #print(f'{len(citations) - i} <= {citations[i]}')
        if len(citations) - i <= citations[i]:
            return len(citations) - i
    return 0
    

print(solution([0, 1, 3, 5, 6]))
print(solution([0, 0, 0, 1]))
print(solution([3,3]))