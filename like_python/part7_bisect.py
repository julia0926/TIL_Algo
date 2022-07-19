import bisect
mylist = [1, 2, 3, 4, 7, 9, 11, 33]
print(bisect.bisect(mylist, 11)) #7
print(bisect.bisect_right(mylist, 11)) #7
print(bisect.bisect_left(mylist, 11)) #6
