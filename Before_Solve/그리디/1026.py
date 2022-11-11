n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
for i in range(n):
    n = min(a) * max(b)
    a.remove(min(a))
    b.remove(max(b))
    result += n

print(result)

