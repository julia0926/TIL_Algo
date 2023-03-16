def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1): #기준값보다 하나 작게 부터 역순으로 내려가며 순회 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)


insert_sort([8,5,6,2,4])