func bubbleSort(_ arr: [Int]) {
    var _arr = arr
    var isSwap = false
    for i in 0..<_arr.count {
        for j in 0..<_arr.count-i-1 {
            
            if _arr[j] > _arr[j+1] {
                _arr.swapAt(j, j+1)
                isSwap = true
            }
        }
        if isSwap == false { return }
    }
    
    print(_arr)
}

bubbleSort([7,5,2,8,1])
