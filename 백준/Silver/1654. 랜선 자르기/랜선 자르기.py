k, piv = map(int,input().split())
lines = []
for i in range(k):
    lines.append(int(input()))


start, end = 1, max(lines)
result = []

# 최대 랜선의 길이 리턴
while start <= end:
    mid = (start+end)//2
    count = 0
    
    for line in lines:
        count += (line // mid)
    # print(mid, count, start, end)
    if count >= piv: 
        start = mid + 1
    else: #n개보다 작게 만들면 포함 안됨.. 
        end = mid - 1

print(end)