#https://leetcode.com/problems/search-in-rotated-sorted-array/
def search(nums, target):
    
    if target not in nums:
        return -1
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]: #왼쪽 범위가 정렬되어있고
            if nums[left] <= target < nums[mid]:#1. 왼쪽 범위내에 target이 존재한다면
                right = mid - 1 #오른쪽 범위를 버릴 수 있음
            else:#2. 왼쪽 범위내에 없으면
                left  = mid + 1 #왼쪽 범위 버림 

        else: #오른쪽 범위가 정렬 
            if nums[mid] < target <= nums[right]: #오른쪽 범위에 target 존재
                left = mid + 1 #왼쪽 범위를 버림 
            else:
                right = mid - 1
        
    return -1
    
 
print(search([4,5,6,7,0,1,2], 0))