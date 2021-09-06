from collections import deque

def bfs(start):
    dq = deque()
    dq.append(start)
    visited[start] = True #1은 방문처리 
    count = 0 #초대할 사람이 몇 명인지 
    depth = 0 #깊이가 2이면 끝 

    while dq:
        depth += 1
        for _ in range(len(dq)):
            friend = dq.popleft()
            for val in list[friend]:
                if not(visited[val]):
                    visited[val] = True
                    dq.append(val)
                    count += 1
        if depth == 2:
            print(count)
            break


n = int(input())
m = int(input())
list = [[] for _ in range(n+1)] #n명의 친구관계를 나타내야 함 
visited = [False] * (n+1)


#양방향 그래프로 연결
for _ in range(m):
    a, b = map(int,input().split())
    list[a].append(b)
    list[b].append(a)

bfs(1)
