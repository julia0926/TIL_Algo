#https://school.programmers.co.kr/learn/courses/30/lessons/17681
#내풀이
def solution(n, arr1, arr2):
    map = []
    for a, b in zip(arr1, arr2):
        result = bin(a | b)[2:]
        if len(result) != n:
            #길이가 n과 다를때 앞에 0을 붙여줬는데, 예를들어 n=5인데 값은 1100일때 01100을 만들어주기 위해
            #내 풀이는 직접 0을 대입해줬으나, 제공하는 모듈 중 rjust라고 오른쪽 정렬하면서 빈 값을 채우는게 있다.
            result = (n-len(result))*"0" + result
            #참고 풀이 : result = result.rjst(n, '0')
        result = result.replace('1', '#').replace('0', ' ')
        map.append(result)
    return map


solution(10, 	[46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])