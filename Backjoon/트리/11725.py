# 실버2 : 트리의 부모 찾기 : https://www.acmicpc.net/problem/11725

from collections import deque


N = int(input())
tree = [[] for _ in range(N+1)]
visited = [0] * (N+1) #방문처리

#양방향 그래프 연결 
for i in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
