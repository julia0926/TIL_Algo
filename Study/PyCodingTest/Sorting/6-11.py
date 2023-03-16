n = int(input())
arr = []

for i in range(n):
    val = input().split()
    arr.append((val[0],int(val[1]))) 

newarr = sorted(arr, key=lambda x: x[1])
for i in newarr:
    print(i[0], end=' ')