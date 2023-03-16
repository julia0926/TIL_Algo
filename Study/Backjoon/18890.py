n = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(list(set(arr)))
answer = []
dic = { sort_arr[i]: i for i in range(len(arr)) }
print(dic)