import heapq

arr = [9, 3, 2, 1, 12]
heapq.heapify(arr)
print(arr)

arr2 = [9, 3, 2, 1, 12, 10]
new_arr = []
for i in arr2:
    heapq.heappush(new_arr, i)
    print(new_arr)
print(new_arr)