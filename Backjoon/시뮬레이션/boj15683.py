'''
0: 빈칸
6: 벽
1~5: CCTV
# : 감시할 수 잇는 영역 
cctv 통과함 
사각지대 : 감시할 수 없는 영역 
'''
from collections import deque

#경우의 수 구하기

n, m = map(int, input().split()) #세로, 가로
answer = 100 #최대 
cctv, graph = [], []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if 1<=graph[i][j]<=5:
            cctv.append((i, j))
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

print(len(cctv))
temp = []


#CCTV 개수에 따른 경우의 수를 구한다. → 백트래킹으로 
#미완성 코드, 내일 다시도전!
def dfs(depth):
    if len(cctv) == depth:
        print(temp)
        return
    for i in range(len(cctv)):
        temp.append(i)
        dfs(depth+1)
        temp.pop()
    
dfs(0)



