# https://www.acmicpc.net/problem/10808
word = input()
alpha = [0] * 26

for w in word:
    alpha[ord(w) - 97] += 1

print(*alpha)