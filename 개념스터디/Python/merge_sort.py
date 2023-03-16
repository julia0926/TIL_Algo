def merge_sort(arr):
    #devide
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    print("분할", left_arr, right_arr)
    #merge
    merge_arr = []
    left = right = 0
    #현재
    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] < right_arr[right]:
            merge_arr.append(left_arr[left])
            left += 1
        else: #오른쪽이 더 작다면 
            merge_arr.append(right_arr[right])
            right += 1
  
    #남아 있는 값 더함 
    merge_arr += left_arr[left:]
    merge_arr += right_arr[right:]
    # print(left_arr[left:],left, right_arr[right:], right)
    return merge_arr

print(merge_sort([21,10,12,20,23,15,22]))