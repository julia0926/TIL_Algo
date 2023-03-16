arr = [5,3,7,6,2,1,4]
def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1] # 피벗은 마지막
    tail = arr[:-1] # 피벗을 제외한 리스트 
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    #각각 왼쪽, 오른쪽 분할정복 하고 정렬된 배열 합쳐서 리턴    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))