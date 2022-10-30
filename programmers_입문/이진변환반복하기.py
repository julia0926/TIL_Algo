#https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    count = 0
    zero = 0
    def make_two(value):
        nonlocal zero, count
        s = value.replace('0', '')
        zero += value.count('0')
        count += 1
        return bin(len(s))[2:]
    while s != '1':
        s = make_two(s)
    return [count, zero]

print(solution("110010101001"))
print(solution("01110"))
# solution("0111010")