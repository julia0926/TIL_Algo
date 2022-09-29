
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def bfs(value):
        visited[value] = True #방문처리
        dq = deque([value]) #큐에 방문한 값을 넣음
        while dq: #큐에 값이 있을 동안
            piv = dq.popleft() #하나를 꺼냄 
            visited[piv] = True #그 값을 방문처리 
            for connect in range(n): #value와 연결되어 있는 컴퓨터를 찾기 위해 
                if connect != value and computers[value][connect] == 1 and not visited[connect]:
                    dq.append(connect)
                    #1. i,i == 1이라했으므로 같으면 안되고
                    #2. 그외의 값이 1인게 연결된 컴퓨터 이므로
                    #3. 그 중 방문하지 않은 컴퓨터라면 
                    #큐에 넣는다. 

    for i in range(n):
        if not visited[i]: #방문하지 않은 컴퓨터라면
            bfs(i)
            answer += 1
    return answer

print(solution(3, 	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))