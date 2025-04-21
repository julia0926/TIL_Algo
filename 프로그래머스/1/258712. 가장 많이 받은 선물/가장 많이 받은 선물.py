from collections import defaultdict
def solution(friends, gifts):
    giver_count = defaultdict(int) # 선물 준 사람
    receiver_count = defaultdict(int) # 선물 받은 사람

    gift_history = defaultdict(lambda: defaultdict(int))
    gift_points = defaultdict(int) # 선물 지수

    for gift in gifts:
        giver, receiver = gift.split()
        giver_count[giver] += 1
        receiver_count[receiver] += 1
        gift_history[giver][receiver] += 1

    for friend in friends:
        point = giver_count[friend] - receiver_count[friend]
        gift_points[friend] = point

    # 다음달에 줄 선물 계산
    next_month_gift = defaultdict(int)

    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            a = friends[i]
            b = friends[j]
            a_to_b = gift_history[a][b]
            b_to_a = gift_history[b][a]
            if a_to_b > b_to_a:
                next_month_gift[a] += 1
            elif a_to_b < b_to_a:
                next_month_gift[b] += 1
            else: #주고받지 않거나 같으면
                if gift_points[a] > gift_points[b]:
                    next_month_gift[a] += 1
                elif gift_points[a] < gift_points[b]:
                    next_month_gift[b] += 1
    
    answer = max(next_month_gift.values(), default=0)
    return answer
