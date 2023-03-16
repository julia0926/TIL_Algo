class CircleQueue:
    def __init__(self,n: int):
        self.n = n
        self.array = [None] * self.n
        self.count = 0
        self.front = 0
        self.rear = 0

    def size(self):
        return self.count

    def is_full(self):
        return self.count == self.n

    def next_index(self, idx):
        return (idx+1) % self.n

    def enqueue(self, data):
        if self.count >= self.n:
            raise Exception('Queue is Full')
        self.array[self.rear] = data #끝에 값을 넣는다
        self.rear = (self.rear + 1) % self.n #원형이므로 n 나눠서
        self.count += 1
        return self.array
    
    def dequeue(self):
        if self.size == 0:
            raise Exception('UnderFlow: 값이 없는데 빼려함')
        temp = self.array[self.front] #첫번째 값 temp에 넣고
        self.array[self.front] = None #제거
        self.front = (self.front+1) % self.n #front 순서를 조정 +1로
        self.count -= 1
        return temp

    def rotate(self):
        print(*self.array)

cQueue = CircleQueue(5)
print(cQueue.size(), cQueue.n)
print(cQueue.enqueue(1))
cQueue.enqueue(2)
cQueue.enqueue(3)
cQueue.enqueue(4)
print(cQueue.enqueue(5))
print(cQueue.is_full())
print("제거",cQueue.dequeue())
print("size",cQueue.size())
cQueue.rotate()



