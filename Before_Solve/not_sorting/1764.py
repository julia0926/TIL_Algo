n, m = map(int, input().split())

no_heard = set(input() for _ in range(n))
no_see = set(input() for _ in range(m))

result = sorted(list(no_heard & no_see))
print(len(result))
for i in result:
    print(i)