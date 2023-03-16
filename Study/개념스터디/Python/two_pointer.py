
n = m = 5

interval_sum = 0
count = 0
end = 0
data = [i for i in range(1, 11)]

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)