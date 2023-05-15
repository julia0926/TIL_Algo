import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    c = int(input())
    arr.append(c)

count, max_cnt = 0, 0 #현재 카운트, 제일 카운트가 많은 개수
max_val = -2 ** 62
arr.sort()

for i in range(n):
    if i == 0 or arr[i-1] == arr[i]:
        count += 1
    else:
        if count > max_cnt: #클때만 갱신하고
            max_cnt = count
            max_val = arr[i-1]
        count = 1 #아니라면 값이 달라졌으므로 그냥 카운트 1

if count > max_cnt:
    max_val = arr[n-1]
print(max_val)
        




