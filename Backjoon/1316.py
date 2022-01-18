n = int(input())
for i in range(n):
    word = input()
    for j in range(1, len(word)):
        #find() 앞 부분 인덱스 리턴 하므로
        if word.find(word[j-1]) > word.find(word[j]):
            #print(word[j-1])
            n -= 1
            break

print(n)