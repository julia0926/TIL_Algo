#브루트 포스
def solution1(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
#in을 통한 탐색
def solution2(nums, target):
    for idx, val in enumerate(nums):
        tem = target - val

        if tem in nums[idx+1:]:
            print(nums[idx+1:].index(tem),(idx+1)) #idx 뒤 배열들 중 tem 값을 찾는데 전체 배열의 인덱스가 아니므로 추가로 idx+1을 더함 
            return [idx, nums[idx+1:].index(tem) + (idx+1)]

#딕셔너리로 계산
def solution3(nums, target):
    nums_map = {}
    
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i

print(solution3([3,2,11,15,6], 9))