#https://www.acmicpc.net/problem/3273
n = int(input())
arr = list(map(int, input().split()))
x = int(input()) #합
#[1, 2, 3, 5, 7, 9, 10, 11, 12]
arr.sort()
start, end = 0, n-1
count = 0

while start < end:
    piv = arr[start] + arr[end]
    if piv == x: 
        count += 1
        start += 1
        end -= 1
    elif piv < x:
        start += 1
    else:
        end -= 1

#조금 개선 4초 빠름 
while start < end:
    piv = arr[start] + arr[end] 
    if piv == x: #값을 찾으면 
        count += 1 #count를 올리고 
    if piv < x: 
        start += 1
        continue
    end -= 1 #끝점을 내린다. (즉, piv >= x 크거나 같으면 )

print(count)



