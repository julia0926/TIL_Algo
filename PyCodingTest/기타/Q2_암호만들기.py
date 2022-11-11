from itertools import combinations

l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()
combi = list(combinations(alpha, l))

'''
1. 최소 1개 모음 + 두개 자음
2. 암호는 증가하는 순서 
'''

for word in combi:
    vowel_cnt = consonants_cnt = 0
    for w in word:
        if w in ['a', 'e', 'i', 'o', 'u']:
            vowel_cnt += 1
        else:
            consonants_cnt += 1
    if vowel_cnt >= 1 and consonants_cnt >= 2:
        print(''.join(word))