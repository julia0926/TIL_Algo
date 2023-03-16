now = input()
row = int(now[1])
col = ord(now[0]) - ord("a") + 1

steps = [(-2,-1),(-2,1),(-1,2),(1,2),(2,-1),(2,1),(-1,-2),(1,-2)]

count = 0
for step in steps:
    nr = row + step[0]
    nc = col + step[1]

    if nr < 1 or nc < 1 or nr > 8 or nc > 8:
        continue
    count += 1

print(count)