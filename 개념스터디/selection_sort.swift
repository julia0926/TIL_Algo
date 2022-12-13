func selectionSort(_ arr: inout [Int])  {
    for i in 0..<(arr.count-1) {
        var minValue = i
        for j in (i+1)..<arr.count {
            if arr[j] < arr[minValue] {
                minValue = j
            }
        }
        arr.swapAt(i, minValue)
    }
    print(arr)

}

var arr = [9,4,3,2,8]
selectionSort(&arr)