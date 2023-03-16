n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]
#구간합 구하기
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 3~4번째 구간 합 구하기
left = 3
right = 4
#오른쪽 - (왼쪽-1)
print(prefix_sum[right] - prefix_sum[left - 1])