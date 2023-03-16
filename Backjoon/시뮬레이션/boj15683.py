'''
0: 빈칸
6: 벽
1~5: CCTV
# : 감시할 수 잇는 영역 
cctv 통과함 
사각지대 : 감시할 수 없는 영역 
'''
import copy
def dfs(graph, depth):
    global answer
    if depth == len(cctv):
        answer = min(answer, count_zero(graph))
        return
    else:
        graph_copy = copy.deepcopy(graph)
        x, y, cctv_type = cctv[depth]
        for cctv_dir in cctv_direction[cctv_type]:
            watch(x, y, cctv_dir,graph_copy)
            dfs(graph_copy, depth + 1) #다른 cctv가 있나 모두 탐색
            graph_copy = copy.deepcopy(graph)


def watch(x, y, dir, graph):
    for d in dir:
        nx, ny = x, y
        while True:
            nx += direction[d][0]
            ny += direction[d][1]
            if 0 <= nx < n and 0 <= ny < y:
                if graph[nx][ny] == 6:
                    continue
                elif graph[nx][ny] == 0:
                    graph[nx][ny] = '#'
            else: #위치 벗어나면 
                break

def count_zero(graph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

n, m = map(int, input().split()) #세로, 가로
answer = 100 #최대 
cctv, graph = [], []
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cctv_direction = [
    [],
    [[0], [1], [2], [3]], # 1번 CCTV
    [[0, 1], [2, 3]], # 2번 CCTV
    [[0, 2], [0, 3], [1, 2], [1, 3]], # 3번 CCTV
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # 4번 CCTV
    [[0, 1, 2, 3]] # 5번 CCTV
]
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if 1<=graph[i][j]<=5:
            cctv.append((i, j, graph[i][j]))
dfs(graph, 0)
print(answer)