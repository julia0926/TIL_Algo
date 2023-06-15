import sys, math
input = sys.stdin.readline

#에라토스 태네스의 체
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True
#팰린드롬 판별
def isPalindrome(v):
    st = str(v)
    if st == st[::-1]:
        return True
    else:
        return False

n = int(input())

while True:
    if isPrime(n) and isPalindrome(n):
        print(n)
        exit(0)
    n+=1