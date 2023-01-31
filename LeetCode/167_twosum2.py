#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

#1. 투포인터 계산
def twoSum(numbers, target):
    left, right = 0, len(numbers)-1
    while left != right:
        print(numbers[left] + numbers[right])
        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            return [left+1, right+1]

#2. 이진 탐색 
def twoSum_bisect(numbers, target):
    for idx, val in enumerate(numbers):
        left, right = idx+1, len(numbers)-1
        expected = target - val #이 값을 찾아야함 
        while left <= right:
            mid = (left+right) // 2
            if numbers[mid] < expected: #더 작으면 왼쪾에 없음
                left = mid + 1
            elif numbers[mid] > expected: 
                right = mid - 1
            else:
                return [idx+1, mid+1]


print(twoSum_bisect([2,7,11,15],9))
# print(twoSum_bisect([2,7,11,15],9))