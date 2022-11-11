# https://www.acmicpc.net/problem/1436

n = int(input())
six_num = 666
cnt = 0

while True:
    if '666' in str(six_num):
        cnt += 1
    if cnt == n:
        print(six_num)
        break
    six_num += 1
    print(six_num)