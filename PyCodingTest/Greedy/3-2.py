n,m,k = map(int,input().split())
arr = list(map(int,input().split())) #n개 입력 

arr.sort(reverse=True)
# 가장 큰 값 k번 두번째 값 1번 
count = (m // k+1 ) * k #수열이 반복되는 횟수
count += m % (k+1) #나누어 떨어지지 않을때
print(count)
result = 0
result += count * arr[0]
result += (m - count) * arr[1]
print(result)
# 풀이 2
# while True:
#     for _ in range(k): # 가장 큰 값 k번 
#         if m == 0: break
#         count += arr[0]
#         m -= 1
#     if m == 0 : break
#     count += arr[1]
#     m -= 1

# print(count)