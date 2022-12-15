# https://www.acmicpc.net/problem/10808
from collections import defaultdict
word = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
dic = defaultdict(int)
for w in word:
    dic[w] += 1

result = []
for a in alpha:
    if a not in dic.keys():
        result.append(0)
    else:
        result.append(dic[a])
print(*result)