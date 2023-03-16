n, b = input().split()

piv = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0

for idx, val in enumerate(n):
    result += (piv.index(val) * pow(int(b),idx))
    
print(result)