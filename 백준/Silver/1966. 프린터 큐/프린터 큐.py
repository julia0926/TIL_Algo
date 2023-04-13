n = int(input())
for _ in range(n):
    n, m = map(int, input().split()) #문서개수, 궁금한 문서 순서
    stack = list(map(int, input().split()))
    stack_idx = list(range(n))
    stack_idx[m] = "target"
    order = 0

    while stack:
        if stack[0] == max(stack):
            order += 1
            if stack_idx[0] == "target":
                print(order)
                break
            else:
                stack.pop(0)
                stack_idx.pop(0)
            
        else:
            stack.append(stack.pop(0)) #가장 뒤로 재배치!
            stack_idx.append(stack_idx.pop(0))