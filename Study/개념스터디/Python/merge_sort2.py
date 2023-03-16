def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    left = right = 0
    result = []

    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] < right_arr[right]:
            result.append(left_arr[left])
            left += 1
        else:
            result.append(right_arr[right])
            right += 1
    
    result += left_arr[left:]
    result += right_arr[right:]
    return result



print(merge_sort([21,10,12,20,23,15,22]))