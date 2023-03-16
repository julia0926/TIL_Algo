def solution(n, m):
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    def lcm(a, b):
        result = (a*b) // gcd(a,b) #두수곱한값 // 최대공약수
        return result

    answer = [gcd(n,m),lcm(n,m)]
    return answer

solution(3, 12)