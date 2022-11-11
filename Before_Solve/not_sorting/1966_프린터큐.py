from collections import deque

case = int(input())

for i in range(case):
    n, m = map(int, input().split())
    priority = deque(map(int, input().split()))
    idx_list = deque(range(n))
    idx_list[m] = 'target'
    order = 0
    
    while True:
        if priority[0] == max(priority):
            order += 1
            if idx_list[0] == 'target':
                print(order)
                break
            else:
                priority.popleft()
                idx_list.popleft()
        else: #앞 숫자가 큰게 아니라면 앞에꺼 빼서 뒤로
            priority.append(priority.popleft())
            idx_list.append(idx_list.popleft())

