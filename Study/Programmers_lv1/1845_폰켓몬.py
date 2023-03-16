#https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    nums_len = len(nums)
    set_len = len(set(nums))
    diff = nums_len - (nums_len - set_len)
    print(diff)
    if diff > len(nums)//2:
        return len(nums)//2
    else:
        return diff

#개간결..!
def solution2(nums):
    return min(len(nums)/2, len(set(nums)))

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2]	)