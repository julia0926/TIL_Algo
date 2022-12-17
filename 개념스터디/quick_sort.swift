func quick_sort(_ arr: [Int]) -> [Int] {
    guard let first = arr.first, arr.count > 1 else { return arr } //배열의 길이가 1개 되면 리턴
    let piv = first
    let left = arr.filter { $0 < piv }
    let right = arr.filter { $0 > piv }
    return quickSort(left) + [piv] + quickSort(right)
    
}