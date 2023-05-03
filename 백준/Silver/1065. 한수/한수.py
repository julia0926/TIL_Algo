n = int(input())


if n < 100:
    print(n)
else: #100보다 크다면 
    count = 99
    for i in range(100, n+1):
        arr = list(map(int, str(i)))
        if arr[0] - arr[1] == arr[1] - arr[2]:
            count += 1
    
    print(count)
