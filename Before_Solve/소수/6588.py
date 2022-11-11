
import enum

check = [True for _ in range(1000001)]
for i in range(2, 1001):
    if check[i]:
        for j in range(i*2, n+1, i):
            check[j] = False

while True:
    n = int(input())
    if n == 0: break
    
                
        
        
            



