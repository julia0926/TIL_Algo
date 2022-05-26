import Foundation

func solution(_ people:[Int]) -> [Int] {
    var counter = [Int: Int]()
    var answer = [Int]()
    people.forEach {
        counter[$0, default: 0] += 1
        if counter[$0]! > 3 {
            answer.append($0)
            counter[$0] = 0
        }
    }
    return answer.isEmpty ? [-1] : answer
}