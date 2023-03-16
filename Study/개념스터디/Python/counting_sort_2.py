#수의 범위가 제한될 때는 매우 효율적이지만, 크면 비효율
from collections import defaultdict

def counting_sort(arr, n):
    dic = {i: 0 for i in range(1, n+1)}
    for v in arr:
        dic[v] += 1
    
    result = []
    for i in range(1, n+1):
        for j in range(dic[i]):
            result.append(i)

    print(result)

counting_sort([1,3,2,4,3,2,5,3,1,2,3,4,4,3,5,1,2,3,5,2,3,1,4,3,5,1,2,1,1,1], 5)