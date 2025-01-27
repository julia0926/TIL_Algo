n = int(input())
m = n #분해합
result = []
while m != 0:
    arr =  [int(char) for char in str(m)]
    if (m + sum(arr)) == n:
        result.append(m)
    m -= 1
        
if result:
    print(min(result))
else:
    print(0)
