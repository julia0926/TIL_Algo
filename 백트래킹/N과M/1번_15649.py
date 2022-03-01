n, m = map(int, input().split())
arr = []
def solve():
    if len(arr) == m:
        print(*arr)
        return
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            solve()
            arr.pop()

solve()

# itertools 사용 
# from itertools import permutations
# n, m = map(int, input().split())

# p = list(permutations(range(1, n+1), m))

# for i in p:
#     print(*i)