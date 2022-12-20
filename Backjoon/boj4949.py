#https://www.acmicpc.net/problem/4949
while True:
    stack = []
    data = input()
    if data == '.':
        break
    flag = True
    for d in data:
        if d == '.': break
        if d == '[' or d == '(':
            stack.append(d)
        elif d == ']':
            if not stack or stack[-1] == '(': #비어있다면 처음것이라는 뜻 or 괄호가 맞지않음 
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop()
                    
        elif d == ')':
            if not stack or stack[-1] == '[':
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop()
        
    if not stack and flag == True:
        print("yes")
    else:
        print("no")

