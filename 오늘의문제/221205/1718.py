#https://www.acmicpc.net/problem/1718
key = input()
text = input()

alpha = " abcdefghijklmnopqrstuvwxyz"

if len(key) > len(text):
    q = len(key) // len(text)
    d = len(key) % len(text)
    text *= q
    text += text[:d]

answer = ""

for k,s in zip(key, text):
    if k != " ":
        val = (alpha.index(k) - alpha.index(s))
        if val <= 0:
            val = 26 + val
        answer += alpha[val]
    else:
        answer += " "

print(answer)

key2 = input()
text2 = input()

answer_ = ""
#더 간단한 풀이
for i in range(len(text2)):
    if text[i] == ' ': answer_ += ' '
    else: answer_ += chr((ord(text2[i]) - ord(key[i%len(key2)]) - 1) % 26 + ord('a'))

print(answer_)