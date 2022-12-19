#최소 힙 구현
class BinaryHeap(object):
    def __init__(self): 
        self.item = [None] #0번째 인덱스를 사용 안하므로 미리 설정
    def __len__(self):
        return len(self.item) - 1
    '''
    삽입
    1. 하위 레벨의 최대한 왼쪽으로 삽입
    2. 부모값과 비교해 더 작은 경우 위치 변경
    3. 반복
    '''
    #업 힙 연산 (내부연산이란 의미로 _붙임)
    def _percolate_up(self): 
        i = len(self)
        parent = i // 2 #절반씩 줄여나가므로 logn 로그만큼 연산 수행 
        while parent > 0:
            if self.items[i] < self.items[parent]: #부모가 더 크다면
                self.items[parent], self.items[i] = \
                    self.items[i], self.items[parent] #값 위치 변경
                # 인덱스도 위치 변경 
                i = parent 
                parent = i // 2
    #삽입
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    #다운 힙 연산
    def _percolate_down(self, idx): 
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]: #왼쪽이 더 작다면 
            smallest = left
        if left <= len(self) and self.items[right] < self.items[smallest]: #왼쪽이 더 작다면 
            smallest = right
        if smallest != idx: #위치가 변경되었으면
            self.items[idx], self.items[smallest] = \
                self.items[smallest], self.items[idx] #값 위치 변경
            self._percolate_down(smallest) #값이 스왑되지 않을 때까지 계속 자식 노드로 내려가면서 swap
    #추출
    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted