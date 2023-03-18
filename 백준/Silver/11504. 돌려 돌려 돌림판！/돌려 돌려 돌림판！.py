T = int(input())
for _ in range(T):
    n, x = map(int, input().split())
    a = int(''.join(list(input().split())))
    b = int(''.join(list(input().split())))
    
    result = 0
    spin_pan = list(input().split()) * 2
    
    for i in range(n):
        num = int(''.join(spin_pan[i:i+x]))
        if a<=num<=b:
            result += 1

    print(result)