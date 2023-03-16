from bisect import bisect_right, bisect_left

a = [1,2,3,4,4,8]
x = 4

print(bisect_left(a,x)) #3
print(bisect_right(a,x)) #5