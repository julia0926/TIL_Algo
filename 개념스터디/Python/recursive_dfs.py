graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}
#재귀
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

print(recursive_dfs(1))

#스택
def iterative_dfs(v):
    discovered = []
    stack = [v] #시작점을 스택에 넣고 
    while stack:
        v = stack.pop()
        if v not in discovered: #방문하지 않았으면 
            discovered.append(v) #넣고
            for w in graph[v]: #인접한 값을 stack에 넣음 
                stack.append(w)
