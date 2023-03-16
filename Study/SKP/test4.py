from itertools import permutations
'''
n개의 차선
m개 전체너비 
차선의 너비는 k이하
'''
def solution(n, m, k):
    paths = list(permutations(list(range(1, k+1)), n))
    if not paths:
        return 0
    for i in range(1, k+1):
        if m == i * n: #똑같은거 n개가 너비일때 
            paths.append((i, i, i))
    
    return len(paths)%1000007

print(solution(3,6,3))
print(solution(10,6,5))