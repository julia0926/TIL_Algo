n = 5 #데이터 개수
m = 5 #찾고자 하는 부분합
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0 #부분 합
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    #부분 합 있을 때는
    if interval_sum == m:
        count += 1

    interval_sum -= data[start] #start를 1 증가

print(count)
