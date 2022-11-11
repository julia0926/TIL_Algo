import sys
input = sys.stdin.readline
arr = []

T = int(input())
for _ in range(T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)] #서류, 면접 성적 입력 
    # 서류 순으로 정렬
    arr.sort(key=lambda x: x[0]) 
    result = 1 #선발된 인원수 (서류 1등은 이미 선발)
    piv = arr[0][1] #서류 1등의 면접 등수가 기준으로 비교 
    for i in range(1, N):
        if piv > arr[i][1]: #기준보다 면접등수가 높으면 (값이 작으면)
            result+=1
            piv = arr[i][1]

    print(result)
