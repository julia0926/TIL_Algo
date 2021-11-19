'''
문제 :
https://programmers.co.kr/learn/courses/30/lessons/82612

참고하면 좋을 코드
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
'''

def solution(price, money, count):
    sum_num = 0
    for i in range(1,count+1):
        sum_num += price * i
    if sum_num > money:
        return sum_num - money
    else:
        return 0

print(solution(3,20,4))