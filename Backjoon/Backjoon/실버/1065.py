# 한수 : https://www.acmicpc.net/problem/1065

n = int(input())
cnt = 99
if n < 100:
    print(n)
elif 100 <= n < 111:
    print(cnt)
else:
    for i in range(111, n+1):
        num_list = list(map(int, str(i))) #자릿수 각각을 정수형으로 바꿔서 리스트에 넣음 
        if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            cnt += 1
    print(cnt)