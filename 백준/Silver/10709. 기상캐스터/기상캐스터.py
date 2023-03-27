h, w = map(int, input().split())
loc = []
cloud = []
for i in range(h):
    line = input()
    for j in range(w):
        if line[j] == 'c':
            loc.append((i, j))
    cloud.append(list(line))

def move(x,y,minute):
    cloud[x][y] = minute
    while y<w-1:
        y += 1
        minute += 1
        cloud[x][y] = minute




for i in range(h):
    for j in range(w):
        if (i, j) in loc:
            move(i,j,0)
        elif cloud[i][j] == '.':
            cloud[i][j] = -1
        

for i in range(h):
    for j in range(w):
        print(cloud[i][j], end=" ")
    print("")