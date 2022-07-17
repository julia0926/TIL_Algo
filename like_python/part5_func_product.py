import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))

#2차원 -> 1차원 리스트로 변환 하기
my_list = [[1, 2], [3, 4], [5, 6]]
print(sum(my_list, []))