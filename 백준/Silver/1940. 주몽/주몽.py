n = int(input())
m = int(input())
arr = sorted(list(map(int, input().split())))

start = 0
end = n-1
result = 0

while start<end:
   sum_v = arr[start]+arr[end]
   if sum_v < m:
      start += 1
   elif sum_v > m:
      end -= 1
   elif sum_v == m:
      result += 1
      end -= 1

print(result)
      