'''
A: 이름
B: 전화번호
P: 하위문자열 
'''

def solution(A, B, P):
    result = []
    for name, num in zip(A, B):
        if P in num:
            result.append(name)
    return sorted(result)[0] if result else "NO CONTACT"

# solution(['pim', 'pom'], ['999999999', '777888999'], '88999')
print(solution(['adam', 'eva', 'leo'], ['121212121', '111111111', '444555666'], '112'))
solution(['sander', 'amy', 'ann', 'michael'], ['123456789', '234567890', '789123456', '123123123'], '1')