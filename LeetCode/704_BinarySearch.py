#https://leetcode.com/problems/binary-search/

#1. 재귀 풀이
def search(nums, target):
    def binary_search(left, right):
        if left<=right:
            mid = (left+right) // 2
            if nums[mid] < target:
                return binary_search(mid+1, right)
            elif nums[mid] > target:
                return binary_search(left, mid-1)
            else:
                return mid
        else:
            return -1

    return binary_search(0, len(nums)-1)

#2. 반복문 풀이
def search2(nums, target):
    left, right = 0, len(nums)-1

    while left<=right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

#3. 이진 검색 모듈
from bisect import bisect_left
def search3(nums, target):
    idx = bisect_left(nums, target)
    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1
    
#4. index 사용
def search4(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1


print(search4([-1,0,3,5,9,12], ))