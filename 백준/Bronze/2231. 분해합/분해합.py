n = int(input())

for i in range(1, n+1):
    num_i = sum(list(map(int, str(i))))
    sum_num = num_i + i
    if sum_num == n:
        print(i)
        break
    if i == n:
        print(0)
    