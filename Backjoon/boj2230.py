#https://www.acmicpc.net/problem/2230
#투포인터, 아니ㅣ ㅣ왜 자꾸 틀려 ?! 맞는데.??!?!?

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

min_result = int(1e9)
arr.sort()
left = right = 0

while left <= right and right < n:
    diff = arr[right]-arr[left]

    if diff < m:
        right += 1
    else:
        min_result = min(min_result,diff)
        left += 1
print(min_result)

