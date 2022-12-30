n, r, c = map(int, input().split()) #2^n개 중 r열 c행
ans = 0
def recursive(x, y, n):
    global ans
    if x == r and y == c:
        print("@@", ans)
        exit(0)
    if n == 1: #재귀의 끝까지 도달했으면
        print(x, y, ans)
        ans += 1
        return
    half = n // 2
    recursive(x, y, half) #1사분면
    recursive(x+half, y, half) #2
    recursive(x, y+half, half) #3
    recursive(x+half, y+half, half) #4

recursive(0, 0, 2 **n)
