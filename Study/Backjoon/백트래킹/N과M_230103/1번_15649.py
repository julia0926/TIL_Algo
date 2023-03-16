N, M = map(int, input().split())
arr = []

def solve():
    if len(arr) == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if not i in arr:
            arr.append(i)
            solve()
            arr.pop()

solve()