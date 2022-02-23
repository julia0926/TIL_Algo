
n = int(input())
arr = list(int(input()) for _ in range(n))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    piv = arr[len(arr) // 2]
    front_arr, equal_arr, back_arr = [], [], []
    for num in arr:
        if num < piv:
            front_arr.append(num)
        elif num == piv:
            equal_arr.append(num)
        else:
            back_arr.append(num)
    return quick_sort(front_arr) + equal_arr + quick_sort(back_arr)

print(quick_sort(arr))
