# https://leetcode.com/problems/design-circular-queue/

#원형큐
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.q1 = 0 #front
        self.q2 = 0 #rear
    
    def enQueue(self, value: int) -> bool:
        if self.q[self.q2] is None: #값이 없다면 
            self.q[self.q2] = value #끝부터 값을 넣음
            self.q2 = (self.q2+1) % self.maxlen #끝 인덱스값 갱신
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.q1] is None: #앞에 빼야할 값이 없다면 none
            return False
        else: #뺄 값 있으면 
            self.q[self.q1] = None #값을 빼고
            self.q1 = (self.q1 + 1) % self.maxlen #front 인덱스 갱신 
            return True

    def Front(self) -> int:
        return -1 if self.q[self.q1] is None else self.q[self.q1]

    def Rear(self) -> int:
        return -1 if self.q[self.q2-1] is None else self.q[self.q2-1]

    def isEmpty(self) -> bool:
        return self.q1 == self.q2 and self.q[self.q1] is None #앞,뒤 인덱스가 같은데 앞 인덱스값이 없으면 아무것도 없음
        
    def isFull(self) -> bool:
        return self.q1 == self.q2 and self.q[self.q1] is not None #앞,뒤 인덱스가 같은데 앞 인덱스값이 있으면 꽉참
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()