#https://www.acmicpc.net/problem/1743
n, m, k = map(int,input().split())
arr = list(list('.' for _ in range(m)) for _ in range(n))
trash = []
for i in range(k):
    a, b = list(map(int, input().split()))
    arr[a-1][b-1] = '#'
    trash.append([a-1, b-1])

result = 0
dir = [[-1,0], [1,0], [0, 1], [0, -1]]

def dfs(x, y, count):
    arr[x][y] = '.' #방문처리
    stack = [(x,y)]
    count += 1
    
    while stack:
        a, b = stack.pop()
        for dx, dy in dir:
            nx = a + dx
            ny = b + dy
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == '#':
                count += 1
                arr[nx][ny] = '.'
                stack.append((nx, ny))
    return count

for a, b in trash:
    result = max(result, dfs(a,b, 0))

print(result)