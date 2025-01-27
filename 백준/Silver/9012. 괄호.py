from collections import deque

n = int(input())
strings = [deque(input()) for _ in range(n)]

for strs in strings:
    first = strs.popleft()
    if first == ')':
        print("NO")
        break
    else:
        stack = []
        for str in strs:
            if str == '(':
                stack.append(str)
            else: # ')'
                if not stack:
                    print("NO")
                    break
                stack.pop()
        if not stack:
            print("YES")
        else:
            print("NO")

        


''''
1
(()())((()))
'''