from itertools import permutations

data = ['A','B','C']
result = list(permutations(data,2))

print(result)

#[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
