n = int(input())
arr = list(map(int, input().split()))

arr.sort()

#중간값 찾기 
print(arr[(n-1) // 2])

# 시간 초과 
# for i in range(1, max(arr) + 1):
#     for j in arr:
#         #print(f'{i} - {j} = {abs(i-j)}')
#         house[i] += abs(i-j)
#     result = min(result, house[i])
# print(result)
