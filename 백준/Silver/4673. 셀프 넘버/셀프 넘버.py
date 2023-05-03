is_self = [False] * 20001

for i in range(1, 10001):
    is_self[i+sum(int(c) for c in str(i))] = True

for i in range(1, 10001):
    if not is_self[i]:
        print(i)