# p.169 퀵 정렬 소스코드

array = [5, 7, 9, 0, 3, 2, 1, 4]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0] #첫번째 원소 기준 
    tail = array[1:] #피벗 제외한 리스트 

    left_side = [x for x in tail if x <= pivot] 
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))