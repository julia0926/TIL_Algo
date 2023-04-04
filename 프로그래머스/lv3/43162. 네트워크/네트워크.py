def solution(n, computers):
    connected = list([0] * n for _ in range(n))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if computers[i][j] == 1 or (computers[i][k] == 1 and computers[k][j] == 1):
                    connected[i][j] = 1
    visited = [False] * n
    total = n-1
    def dfs(x):
        visited[x] = True
        stack = [x]
        while stack:
            v = stack.pop()
            for i in range(n):
                if i != v and not visited[i] and connected[i][v] == connected[v][i] == 1:
                    # print(v,i, connected[i][total-i],connected[total-i][i]  )
                    stack.append(i)
                    visited[i] = True
    result = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            result += 1
    # print(result)
    return result