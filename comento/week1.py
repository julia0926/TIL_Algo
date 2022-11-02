from operator import le
from re import L


def insert_sort(arr):
    for j in range(1, len(arr)):
        for i in range(j, 0, -1):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i],arr[i-1]
    print(arr)

insert_sort([3,2,1,5,66,2])

def merge_sort(arr): #T(n)
    if len(arr) == 1: #θ(1) -> 단순 리턴 
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid]) # 2T(n/2)
    right = merge_sort(arr[mid:])  # 2T(n/2)
    l = h = 0
    result = [] #θ(n)

    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[h])
            h += 1
    result += left[l:]
    result += right[h:]
    return result

print(merge_sort([1,2,42,12,12,-1, 3]))

def heapify(unsorted, index, heap_size):
    largest = index
    left_idx = 2 * index + 1
    right_idx = 2 * index + 2
    if left_idx < heap_size and unsorted[left_idx] > unsorted[largest]:
        largest = left_idx
    if right_idx < heap_size and unsorted[right_idx] > unsorted[largest]:
        largest = right_idx
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest] #swap
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
    length = len(unsorted)
    for i in range(length // 2 - 1, -1, -1):
        heapify(unsorted, i, length)
    for i in range(length-1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted

print(heap_sort([1,2,42,12,12,-1, 3]))

