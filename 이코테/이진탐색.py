def binary(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary(array, target, mid+1, end)
    else:
        return binary(array, target, start, mid-1)        

# print(binary([1,3,5,8,9], 8, 0, 4))


from bisect import bisect_left, bisect_right

def count_by_range(a, left, right):
    right_idx = bisect_right(a, right)
    left_idx = bisect_left(a, left)
    return right_idx - left_idx

a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a, 1,4))