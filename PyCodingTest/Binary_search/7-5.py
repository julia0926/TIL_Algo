from cgitb import reset


def binary_serach(array, target):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = ( start + end ) // 2
        if target > array[mid]:
            start = mid + 1
        elif target == array[mid]:
            return "yes"
        else:
            end = mid - 1
    return "no"

n = int(input())
shop_thing = list(map(int,input().split()))
m = int(input())
customer_thing = list(map(int,input().split()))
shop_thing.sort()

result = ""
for val in customer_thing:
    #이진 탐색 구현
    result += binary_serach(shop_thing, val) + " "
print(result)