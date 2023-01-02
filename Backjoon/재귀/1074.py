n, r, c = map(int, input().split()) #2^n개 중 r열 c행

def recursive(n, x, y):
    if n == 0:  return 0
    half = pow(2, n-1)
    if x < half and y < half: #1사분면 
        return recursive(n-1, x, y)
    if x < half and y >= half: #2사분면 
        return half*half + recursive(n-1, x, y-half) #시작점을 더하고 + y값을 갱신 
    if x >= half and y < half: #3사분면 
        return 2*half*half + recursive(n-1,x-half, y)
    if x >= half and y >= half:
        return 3*half*half + recursive(n-1,x-half,y-half)

#시작점을 갱신시키면서 분할정복
print(recursive(n, r, c)) 
