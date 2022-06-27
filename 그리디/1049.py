# 실버 5 - 기타줄 : https://www.acmicpc.net/problem/1049
n, m = map(int, input().split()) #필요 개수
list = []
result = 0
min_pack, min_val = 1001, 1001
for i in range(m):
    a, b = map(int, input().split()) #패키지, 낱개
    min_pack = min(min_pack, a)
    min_val = min(min_val, b)

# 낱개가 더 쌀 경우 
if min_val * 6 < min_pack:
    print(min_val * n)
# 패키지로 산다음에 나머지를 1. 묶음, 2. 낱개 
else:
    result = (n // 6) * min_pack
    #나머지를 어떻게 살껀지? n%6
    #1. 패키지가 싸다 
    if (n % 6) * min_val > min_pack:
        result += min_pack
    else: #낱개가 싸다
        result += (n % 6) * min_val
    print(result)
