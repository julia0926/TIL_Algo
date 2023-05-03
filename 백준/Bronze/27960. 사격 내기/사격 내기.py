a, b = map(int, input().split())

result = ''
a, b = format(a, 'b'), format(b, 'b')
max_len = max(len(a), len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)


for i, j in zip(a, b):
    if i != j:
        result += '1'
    else:
        result += '0'

print(int(result, 2))

