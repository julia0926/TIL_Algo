func CountingSort(_ arr: [Int], _ rg: Int) -> [Int] {
    var countArr: [Int: Int] = [:]
    //초기 생성 
    for i in 1...rg {
        countArr[i] = 0
    }
    for i in 0..<arr.count {
        countArr[arr[i]]! += 1
    }
    var result: [Int] = []
    for i in 1...rg {
        for _ in 0..<countArr[i]! {
            result.append(i)
        }
    }

    return result
}

CountingSort([1,3,2,4,3,2,5,3,1,2,3,4,4,3,5,1,2,3,5,2,3,1,4,3,5,1,2,1,1,1], 5)
