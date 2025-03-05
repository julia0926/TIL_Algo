n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()
# print(a,b)

result = sum(x*y for x, y in zip(a, b))
print(result)