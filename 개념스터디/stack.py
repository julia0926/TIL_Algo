class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next 

#연결리스트로 구현 
class Stack:
    def __init__(self):
        self.last = None #처음 시작은 없음 
    
    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item #마지막의 item값 꺼내두고
        self.last = self.last.next #다음 값을 마지막으로
        return item


stack = Stack()
stack.push(1)
stack.push(5)
stack.push(3)
print(stack.pop())
print(stack.pop())