n = int(input())
home = [list(map(int,input().split())) for _ in range(n)]


for i in range(1, n):
    for j in range(3):
        if j == 0:
            home[i][j] = home[i][j] + min(home[i-1][j+1], home[i-1][j+2])
        elif j == 1:
            home[i][j] = home[i][j] + min(home[i-1][j-1], home[i-1][j+1])
        else:
            home[i][j] = home[i][j] + min(home[i-1][j-1], home[i-1][j-2])
        #print(home[i][j])

print(min(home[n-1][0], home[n-1][1], home[n-1][2]))


# 1차
# n = int(input())
# home = [list(map(int,input().split())) for _ in range(n)]
# d = [[0] * 3 for _ in range(n)]

# d[0][0] = home[0][0]
# d[0][1] = home[0][1]
# d[0][2] = home[0][2]


# for i in range(1, n):
#     for j in range(3):
#         if j == 0:
#             d[i][j] = home[i][j] + min(d[i-1][j+1], d[i-1][j+2])
#         elif j == 1:
#             d[i][j] = home[i][j] + min(d[i-1][j-1], d[i-1][j+1])
#         else:
#             d[i][j] = home[i][j] + min(d[i-1][j-1], d[i-1][j-2])
#         #print(d[i][j])

# print(min(d[n-1][0], d[n-1][1], d[n-1][2]))