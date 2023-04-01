from collections import defaultdict

def solution(n, wires):
    dic = defaultdict(list)
    for wire in wires:
        a, b = wire
        dic[a].append(b)
        dic[b].append(a)
    
    def dfs(node):
        count = 1
        visited = [False] * (n+1)
        visited[node] = True
        stack = [node]
        
        while stack:
            value = stack.pop()
            for v in dic[value]:
                if not visited[v]:
                    stack.append(v)
                    visited[v] = True
                    count += 1
        return count
        
    
    result = []
    for wire in wires:
        a, b = wire
        #끊는다.
        dic[a].remove(b)
        dic[b].remove(a)
        #송전탑 개수 탐색.
        result.append(abs(dfs(a)-dfs(b)))
        #다시 연결한다.
        dic[a].append(b)
        dic[b].append(a)

    return min(result)