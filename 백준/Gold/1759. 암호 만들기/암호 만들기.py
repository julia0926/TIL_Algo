n, m = map(int, input().split())
arr = sorted(list(input().split()))
vowels = ['a','e','i','o','u']
result = []
def dfs(start):
    if len(result) == n:
        count = sum(result.count(v) for v in vowels)
        if count >= 1 and n - count >= 2:
            print(''.join(result))
            return
    for i in range(start, m):
        if arr[i] not in result: #중복 제거
            #모음이 최소 한개
            result.append(arr[i])
            dfs(i+1)
            result.pop()

dfs(0)