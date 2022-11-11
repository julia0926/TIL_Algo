arr = [[0, 0, 1, 0, 0, 1],
            [0, 1, 0, 2, 0, 0],
            [0, 0, 2, 6, 12, 1],
            [0, 1, 0, 3, 0, 0], 
            [0, 9, 0, 0, 4, 0]]


print(list(map(max,arr)))
print(max(list(map(max,arr))))

print(list(map(lambda x: x+1, [20,23])))