#https://www.acmicpc.net/problem/21921

n, x = map(int, input().split())
arr = list(map(int, input().split()))

'''
출력 : X일동안 가장 많이 들어온 방문자수 
기간이 몇개 ?
'''
if arr.count(0) == n:
    print("SAD")
else:
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = dp[i-1] + arr[i]
    visitor = [dp[x-1]]
    
    for i in range(x, n):
        visitor.append(dp[i] - dp[i-x])
    max_visitor = max(visitor)
    print(max_visitor)
    print(visitor.count(max_visitor))
    
        
        

