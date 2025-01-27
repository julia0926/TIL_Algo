n = int(input())
arr = [i for i in range(1, n+1)]
check = [False] * n
choose = []

def permutation(level):
    if level == n:
        print(*choose)
        return
    
    for i in range(n):
        if check[i]: #인덱스 i가 이미 쓰이고 있으면 무시
            continue
        choose.append(arr[i])
        check[i] = True
        permutation(level+1)

        check[i] = False
        choose.pop()

permutation(0)
