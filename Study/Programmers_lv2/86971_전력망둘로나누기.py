from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    def bfs(start): #시작점의 송전탑개수를 리턴 
        visited[start] = True
        dq = deque([start])
        result = 1
        while dq:
            now = dq.popleft() #노드를 하나 꺼내고 
            for i in graph[now]:
                if not visited[i]:
                    result += 1 #개수를 센다.
                    dq.append(i)
                    visited[i] = True 
        return result

    result_arr = []
    for start, not_visit in wires:
        visited = [False] * (n+1)
        visited[not_visit] = True #이게 끊어버리는 역할이다 !
        first_top = bfs(start)
        result_arr.append(abs((n- first_top) - first_top))

    #제일 큰값
    return min(result_arr)

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
