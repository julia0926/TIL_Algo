import UIKit

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var result = [Int]()
    for val in commands {
        let i = val[0] - 1
        let j = val[1] - 1
        let k = val[2]
        result.append(array[i...j].sorted()[k-1])
    }
    return result
}

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

