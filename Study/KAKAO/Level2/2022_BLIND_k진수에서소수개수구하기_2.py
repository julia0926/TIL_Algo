def change(n, k):
    result = ''
    while n:
        n, mod = divmod(n, k) #주의 ! 여기서 
        result += str(mod)
    return result[::-1]

def get_sosu(n):
    if n == 1: return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0: return False
    return True

def solution(n, k):
    value = change(n, k)
    answer = 0
    for i in value.split('0'):
        if i == '': continue
        if get_sosu(int(i)): answer += 1
    return answer

print(solution(437674, 3))
print(solution(110011, 10))