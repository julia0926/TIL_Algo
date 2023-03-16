n, m = map(int, input().split())
result = []

#중복을 제거 해야함 
def dfs(v):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return 
    
    for i in range(v, n+1): #1, n+1까지 
        if i not in result:
            result.append(i)
            dfs(i+1) #2가 돌아감 
            result.pop() 

dfs(1) #1부터 시작 이라면 