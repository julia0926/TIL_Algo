n, m = map(int, input().split())
nlist = list(map(int, input().split()))

nlist.sort()
s = []
def dfs():
    if len(s) == m:
        print(*s)
        return
    for value in nlist:
        # print(value)
        if value not in s:
            s.append(value)
            dfs()
            s.pop()

dfs()