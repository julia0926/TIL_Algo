def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2 #중간 값을 리턴
        if array[mid] > target: #왼쪽을 봐야됨
            end = mid - 1
        elif array[mid] < target: 
            start = mid + 1
        else:
            return mid
    return None #찾는 값이 없으면 

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1) 