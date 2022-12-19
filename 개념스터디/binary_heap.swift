
struct Heap<T: Comparable> {
    var heap: Array<T> = []
    init() { }
    init(data: T) {
        heap.append(data) //heap은 1번쨰부터 시작하므로 0 채우고
        heap.append(data) //실제 Root Node 채우기 
    }
    
    mutating func insert(_ data: T) {
        if heap.count == 0 {
            heap.append(0)
            heap.append(data)
            return
        }
        heap.append(data)
        func isMoveUp(_ insertIdx: Int) -> Bool {
            if insertIdx <= 1 {
                return false //루트 노드라면 더이상 올라가지 않아도 되므로
            }
            let parentIdx: Int = idx / 2
            return heap[insertIdx] > heap[parentIdx] ? true : false //삽입할 인덱스가 더 크단뜻은 더 탐색할 노드가 있다.
        }
        var insertIdx: Int = heap.count - 1
        while isMoveUp(insertIdx) { 
            let parentIdx: Int = insertIdx / 2
            heap.swapAt(insertIdx, parentIdx)
            insertIdx = parentIdx //탐색할 인덱스 갱신 
        }
    }
    
}

