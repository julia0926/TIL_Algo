n = int(input())
shop_thing = set(map(int,input().split())) #중복 값을 없애고 순서 상관 없음
m = int(input())
customer_thing = list(map(int,input().split()))

print(shop_thing)
for i in customer_thing:
    if i in shop_thing:
        print('yes', end=' ')
    else:
        print('no', end=' ')