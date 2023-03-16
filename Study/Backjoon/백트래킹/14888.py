n = int(input())
values = list(map(int,input().split()))
op = list(map(int,input().split()))
max_val = -1e9
min_val = 1e9

def dfs(depth, result, plus, minus, multiply, divide):
    global max_val, min_val
    if depth == n:
        max_val = max(result, max_val)
        min_val = min(result, min_val)
        return 
    if plus:
        dfs(depth+1, result+values[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, result-values[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, result*values[depth], plus, minus, multiply-1, divide)
    if divide:
        if result < 0: #음수라면
            dfs(depth+1, -(-(result)//values[depth]), plus, minus, multiply, divide-1)
        else:
            dfs(depth+1, result//values[depth] , plus, minus, multiply, divide-1)

dfs(1, values[0], op[0], op[1], op[2], op[3])
print(max_val)
print(min_val)