import sys

class Node:
    def __init__(self, value=0, end=False):
        self.value = value
        self.end=end
        self.children = []
    
    def __str__(self):
        return f'{self.value} {self.end}'

def insert(root, num): #빈노드, 숫자 
    current = root
    i = 0
    while i < len(num):
        exist = False
        for j in range(len(current.children)): #자식 노드만큼 돈다
            child = current.children[j]
            if num[i] == child.value: #자식의 값과 같으면 
                exist = True #접두어 있다.
                break
            if exist: #접두어가 있으면 끝값도 같은지 비교 
                if current.children[j].end:
                    return True #띠용?
                current = current.children[j] #같은문자가 있으면 해당 노드로 이동 
            else: #같은 문자가 없으면 노드를 새로 생성..
                current.children.append(Node(num[i], i==len(num)-1))
                current = current.children[-1]
            i += 1
    return False


def solution():
    read = sys.stdin.readline
    t = int(read())
    
    for _ in range(t):
        n = int(read())
        phonebook = [list(read().rstrip()) for _ in range(n)] #하나씩 쪼개서 
        phonebook.sort(key=len)
        print(phonebook)


solution()