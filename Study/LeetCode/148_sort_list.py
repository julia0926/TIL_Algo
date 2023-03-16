#https://leetcode.com/problems/sort-colors/
def sortColors(nums):
    red, white, blue = 0, 0, len(nums)

    while white < blue:
        if nums[white] < 1:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] > 1:
            blue -= 1
            nums[white], nums[blue] = nums[blue], nums[white]
        else: #1과 같으면
            white += 1
    print(nums)

sortColors([2,0,2,1,1,0])


