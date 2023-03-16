def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int,input().split()) #노드, 간선 
parent = [0] * (v+1) #부모 테이블

edges = [] #모든 간선을 담을 리스트 
result = 0 #부모 테이블 초기화

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost, a, b))
    
edges.sort() #간선을 비용순으로 정렬

for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만, 즉, 같은 집합 내에 포함되지 않으면 
    if find_parent(parent, a) != find_parent(parent, b): 
        union_parent(parent, a, b)
        result += cost

print(result)