from collections import Counter

def back_tracking(length, prev_char):
    answer = 0
    if length == len(st):
        return 1
    for char in counter:
        if counter[char] > 0 and char != prev_char:
            counter[char] -= 1
            answer += back_tracking(length+1, char)
            counter[char] += 1
    return answer

st = input()
counter = Counter(st)
print(back_tracking(0, ''))

