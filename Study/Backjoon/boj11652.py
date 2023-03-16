n = int(input())
cards = []

for i in range(n):
    cards.append(int(input()))

cnt, max_cnt = 0, 0
max_val = -1e9
cards.sort()

for idx in range(1, len(cards)):
    if cards[idx-1] == cards[idx]:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
            max_val = cards[idx-1]
        cnt = 1

# if cnt > max_cnt: max_val = cards[n-1] #제일 마지막도 계산해야함
print(max_val)

    
