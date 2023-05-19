import sys
input = sys.stdin.readline

n = int(input().rstrip())

def solution(string):
    cnt = 0
    for st in string:
        if st == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return "NO"
    if cnt == 0:
        return "YES"
    else:
        return "NO"

for _ in range(n):
    string = input().rstrip()
    print(solution(string))