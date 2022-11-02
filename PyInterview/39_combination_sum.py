'''
숫자집합 candinates를 조합해서 target이 되는 원소를 나열 
'''

def solution(candinates, target):
    result = []
    def dfs(csum, index, path): #갱신합, 순서, 지금까지 탐색 경로
        if csum < 0:
            return
        if csum == 0: #딱 종료 조건이라면
            result.append(path)
            print("append!!", path, result)
            return
        
        for i in range(index, len(candinates)): #인덱스부터 길이까지
            print(csum-candinates[i], i, candinates[i])
            dfs(csum-candinates[i], i, path + [candinates[i]])

    dfs(target, 0, [])
    return result
print(solution([2,3,6,7], 7))