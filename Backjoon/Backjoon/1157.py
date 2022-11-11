word = input()
word = word.upper()
max_val = 0
index = 0
result = '?'
alpha = [0] * 24

for i in range(len(word)):
    index = ord(word[i]) - 65
    #print(index)
    alpha[index] += 1
    if max_val < alpha[index]:
        max_val = alpha[index]
        result = word[i]
    elif max_val == alpha[index]:
        result = '?'

print(result)

