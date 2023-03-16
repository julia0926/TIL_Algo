#https://www.acmicpc.net/problem/9046

'''
시도: Counter 사용하려 했는데, 계속 런타임에러(ValueError) 발생
그래서, 그냥 a~z까지 개수 count하고 아스키코드로 처리했다.
'''

# for _ in range(t):
#     v = input().replace(' ', '')
#     c1, c2 = Counter(v).most_common(2)
#     if c1[1] == c2[1]:
#         print('?')
#     else:
#         print(str(c1[0]))
t = int(input())

for _ in range(t):
    word = input().replace(' ', '')
    dic = [0] * 26

    for i in word:
        dic[ord(i)-97] += 1
    max_val = max(dic)
    if dic.count(max_val) > 1:
        print('?')
    else:
        print(chr(97+dic.index(max_val)))