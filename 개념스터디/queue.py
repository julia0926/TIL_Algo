class Queue:
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def insert(self, item):
        self.entries.append(item)

    def pop(self):
        if self.entries: #값이 존재하면
            value = self.entries[0]
            self.entries = self.entries[1:]
        else:
            print("Queue is Empty")

        return value
    
    #모든 원소 순회
    def rotate(self):
        for i in range(len(self.entries)):
            print(self.entries[i], end=' ')
        
    def size(self):
        return len(self.entries)

queue = Queue()
queue.insert(1)
queue.insert(3)
queue.insert(4)
print("pop", queue.pop())
print(queue.rotate())
print(queue.size())

