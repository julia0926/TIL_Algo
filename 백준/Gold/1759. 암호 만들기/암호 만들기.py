from itertools import combinations

pick, total = map(int, input().split())
arr = sorted(list(input().split()))

word_list = []
result = []


def check(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = sum(1 for char in word if char in vowels)
    const_count = len(word) - vowel_count
    return vowel_count >= 1 and const_count >= 2


for combi in list(combinations(arr, pick)):
    if check(combi):
        print(''.join(combi))
