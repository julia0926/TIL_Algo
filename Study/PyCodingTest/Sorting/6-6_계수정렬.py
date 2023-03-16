# p.174 계수 정렬

array = [5, 7, 9, 0, 3, 2, 1, 4, 3, 3, 1, 9]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스 값 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
