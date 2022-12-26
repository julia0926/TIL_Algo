def counting_sort(arr, rg):
    count = {i: 0 for i in range(1, rg+1)}
    for num in arr:
        count[num] += 1
    result = []
    for i in range(1, rg+1):
        for _ in range(count[i]):
            result.append(i)
    print(result)


counting_sort([1,3,2,4,3,2,5,3,1,2,3,4,4,3,5,1,2,3,5,2,3,1,4,3,5,1,2,1,1,1], 5)