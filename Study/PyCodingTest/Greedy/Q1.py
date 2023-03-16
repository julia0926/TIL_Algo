from numpy import sort


N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0 #총 그룹의 수
count = 0 # 현재 그룹의 명 수 
for i in arr:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)




# 첫번째 시도 : 모두 그룹에 들어가야 되는 줄 알고 작성함
# while len(arr) != 0:
#     for _ in range(max(arr)):
#         arr.pop()
#     count += 1
# print(count)

