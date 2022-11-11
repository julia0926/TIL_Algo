# 실버3 : 색종이 만들기 https://www.acmicpc.net/problem/2630

n = int(input())
paper = list(list(map(int, input().split())) for _ in range(n))
result = []
def solution(x, y, size):
    color = paper[x][y] #첫번째 값 
    half = size // 2
    for i in range(x, x+size):
        for j in range(y, y+size):
            if color != paper[i][j]: #첫번째 값과 다르다면
                print(f'{i}, {j} : {color} - {paper[i][j]}')
                solution(x, y, half)
                solution(x+half, y, half)
                solution(x, y+half, half)
                solution(x+half, y+half, half)
                return 
    result.append(1) if color == 1 else result.append(0)
    
                
solution(0,0,n)



