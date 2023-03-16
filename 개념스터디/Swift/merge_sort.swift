func mergeSort(_ arr: [Int]) -> [Int] {
    if arr.count < 2 {
        return arr
    }
    let mid = arr.count / 2
    let leftArr = mergeSort(Array(arr[0..<mid]))
    let rightArr = mergeSort(Array(arr[mid..<arr.count]))
    
    func merge(_ left: [Int], _ right: [Int]) -> [Int] {
        var left = left
        var right = right
        var result: [Int] = []
        
        while !left.isEmpty && !right.isEmpty { 
            //더 작은 값을 제거하면서 result에 더해줌 -> merge 단계
            if left[0] < right[0] {
                result.append(left.removeFirst())
            } else {
                result.append(right.removeFirst())
            }
        }
        
        if !left.isEmpty {
            result.append(contentsOf: left) //result에 남아있는 left 배열 더함
        } 
        if !right.isEmpty {
            result.append(contentsOf: right) 
        }
        return result
    }
    return merge(leftArr, rightArr)
}

print(mergeSort([21,10,12,20,23,15,22]))