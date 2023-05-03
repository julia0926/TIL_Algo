
self_num = []
for i in range(1, 10001):
    self_num.append((sum(list(map(int, str(i)))) + i))

for i in range(1, 10001):
    if i not in self_num:
        print(i)