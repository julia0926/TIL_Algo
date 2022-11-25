#https://www.acmicpc.net/problem/3005

r, c = map(int, input().split())

arr = [ list(input()) for _ in range(r)]
words = []
#가로 
for i in range(r):
    word = ""
    for j in range(c):
        if arr[i][j] != '#': 
            word += arr[i][j]
        else: 
            if len(word) > 1:
                words.append(word)
            word = ""
 
    if word != '' and len(word) > 1: words.append(word)
new_list = list(map(list, zip(*arr)))

#세로
for i in range(c):
    word = ""
    for j in range(r):
        if new_list[i][j] != '#': 
            word += new_list[i][j]
        else: 
            if len(word) > 1:
                words.append(word)
            word = ""
 
    if word != '' and len(word) > 1: words.append(word)
print(sorted(words)[0])
