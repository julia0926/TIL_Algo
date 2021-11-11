from itertools import combinations

data = ['A','B','C']

result2 = list(combinations(data,2))
print(result2)
#[('A', 'B'), ('A', 'C'), ('B', 'C')]
