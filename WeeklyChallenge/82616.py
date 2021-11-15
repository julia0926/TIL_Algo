# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    sum_num = 0
    for i in range(1,count+1):
        new = price * i
        sum_num += new
    if sum_num > money:
        return sum_num - money
    else:
        return 0

print(solution(3,20,4))