def selection_sort(arr):
    for i in range(len(arr)-1): #arr길이의 -1까지 range
        min_val = i #i부터 비교 
        for j in range(i+1, len(arr)): #i+1~arr 까지 비교하면서 
            if arr[j] < arr[min_val]: #min_val 값보다 작은 값을 발견했다면 
                min_val = j #인덱스 값을 저장 
        arr[min_val], arr[i] = arr[i], arr[min_val] #가장작은값 담긴 인덱스와 현재i값 swap
    return arr

print(selection_sort([9,6,7,3,5]))