'''
0: 빈칸
6: 벽
1~5: CCTV
# : 감시할 수 잇는 영역 
cctv 통과함 
사각지대 : 감시할 수 없는 영역 
'''

n, m = map(int, input().split()) #세로, 가로
answer = 100 #최대 
cctv, graph = [], []
cctv_dir = []
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
observer_dir = [0,4,2,4,4,1]
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if 1<=graph[i][j]<=5:
            cctv.append((graph[i][j]))
            cctv_dir.append(observer_dir[graph[i][j]])
print(cctv_dir)

def dfs(x, ans):
    if x!=0 and not ans:
        return
    if x == len(cctv):
        print(ans)
        return
    for i in range(cctv_dir[x]):
        ans.append(i)
        dfs(x+1, ans)
        ans.pop()
dfs(0, [])
'''
길이 = 3
[2,2,1]
0,0,0
0,1,0
1,0,0
1,1,0

'''