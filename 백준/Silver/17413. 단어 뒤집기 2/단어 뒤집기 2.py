str = input()
flag = False #닫힘<> , true면 열림 < 
stack = []
result = ""
word = ""

for val in str:
    if val == " ":
        while stack:
            result += stack.pop()
        result += val
    elif val == "<":
        while stack:
            result += stack.pop()
        flag = True
        result += val
    elif val == ">":
        flag = False
        result += val
    elif flag: #괄호가 열려있으면 그냥 값을 추가함 
        result += val

    #괄호 밖은 단어를 뒤집음 
    else:
        stack.append(val)

while stack:
    result += stack.pop()
    
print(result)    


