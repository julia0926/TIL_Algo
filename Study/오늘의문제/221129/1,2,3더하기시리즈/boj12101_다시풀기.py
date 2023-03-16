n, k = map(int, input().split())

def dfs(idx, sum_val, arr):
    if sum_val > n:
        return
    if sum_val == n:
        
    for i in range(1, 4):
        arr.append(str(i)+'+')
        dfs(idx+1, sum_val+i, arr)
        arr.pop()
