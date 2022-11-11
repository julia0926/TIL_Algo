# 실버3 - 시리얼번호 : https://www.acmicpc.net/problem/1431
# 다중 조건 정렬에 대해 복습하였다.

def sum_num(list):
    result = 0
    for i in list:
        if i.isdigit():
            result += int(i)
    return result

    

n = int(input())
arr = []
for i in range(n):
    arr.append(input())

arr.sort(key=lambda x:(len(x), sum_num(x), x))
for i in arr:
    print(i)
