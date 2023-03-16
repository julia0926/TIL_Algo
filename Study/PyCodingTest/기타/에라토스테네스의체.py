import math
from string import octdigits

n = 100
array = [True for _ in range(n+1)]

for i in range(2, int(math.sqrt(n))):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False #소수가 아님 
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')