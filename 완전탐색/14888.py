n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))
result = []
def dfs(value, depth, plus, minus, multi, divide):
    if depth == len(arr):
        result.append(value)
        return
    if plus > 0:
        dfs(value+arr[depth], depth+1, plus-1, minus, multi, divide)
    if minus > 0:
        dfs(value-arr[depth], depth+1, plus, minus-1, multi, divide)
    if multi > 0:
        dfs(value*arr[depth], depth+1, plus, minus, multi-1, divide)
    if divide > 0:
        if value < 0:
            dfs(-(-value//arr[depth]), depth+1, plus, minus, multi, divide-1)
        else:
            dfs(value//arr[depth], depth+1, plus, minus, multi, divide-1)


dfs(arr[0], 1, op[0], op[1], op[2], op[3])
print(max(result))
print(min(result))