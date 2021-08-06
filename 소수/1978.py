prime = [False, False] + [True] * 10000

#소수를 구하기 위함
for i in range(2, 101): #
    if prime[i]: #2보다 크면 True라면 
        for j in range(i*2, 10001, i): #10000까지
            prime[j] = False

n = int(input())

for _ in range(n):
    V = int(input())
    #에라테노스 체에서 소수를 구할 때 절반 이상의 값을 나눠도 나머지가 0이 나올수가 없음
    A = V // 2 
    B = A
    for _ in range(10000):
        if prime[A] and prime[B]:
            print(A, B)
            break
        A -= 1
        B += 1