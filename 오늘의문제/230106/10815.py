#https://www.acmicpc.net/problem/10815
n = int(input())
card = sorted(list(map(int, input().split())))
#상근이가 가지고 있는 숫자카드인지 아닌지 비교
m = int(input())
piv_card = list(map(int, input().split()))

result = []
result2 = []

def search(target):
    left, right = 0, len(card)-1
    while left<=right:
        mid = (left+right)//2
        if card[mid] < target: #오른쪽에 있다
            left = mid+1 #시작점 조정
        elif card[mid] > target: #왼쪾에 있따
            right = mid - 1
        else:
            return 1
    return 0

#이진탐색 모듈 사용 
from bisect import bisect_left
def module_insect(target):
    idx = bisect_left(card, target)
    if idx < len(card) and card[idx] == target:
        return 1
    return 0


for piv in piv_card:
    result.append(search(piv))
    result2.append(module_insect(piv))

# print(*result)
print(*result2)
