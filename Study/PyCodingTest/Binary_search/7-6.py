n = int(input())

array = [0] * 1000001
for i in input().split():
    array[int(i)] = 1 #해당 인덱스에 값을 기록

m = int(input())
customer_thing = list(map(int,input().split()))

for i in customer_thing:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')