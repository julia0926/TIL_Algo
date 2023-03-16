n, s = map(int, input().split())
arr = list(map(int, input().split()))
# visited = [False] * n
# result = 0

# #첫번째 시도 -> 시간초과 
# def solve(depth, total):
#     global result
#     if total == s: #기준 값이 다 더한값 s와 같으면 
#         result += 1
#         return
#     if depth == n: 
#         return 
#     for i in range(n):
#         visited[i] = True
#         total += arr[i]
#         solve(depth+1, total)
#         visited[i] = False
#         total -= arr[i]

# solve(0, 0)
# print(result)

#2번째 시도(바킹독 참고)
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
def solve2(depth, total):
    global cnt
    if depth == n:
        if total == s:
            cnt += 1
        return
    solve2(depth+1, total) #안더했을 때
    solve2(depth+1, total+arr[depth]) #더했을 때

solve2(0,0)
print(cnt if s != 0 else cnt-1) #공집합을 빼줘야함 (양수만 구한다고 조건에 있기때문 