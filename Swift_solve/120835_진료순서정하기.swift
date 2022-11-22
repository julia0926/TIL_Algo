//https://school.programmers.co.kr/learn/courses/30/lessons/120835

//내 풀이 
import Foundation

func solution(_ emergency:[Int]) -> [Int] {
    var result: [Int] = []
    var sortArr = emergency.sorted(by: >)
    for val in emergency {
        let idx = sortArr.firstIndex(of: val)!
        result.append(idx+1)
    }
    return result
}

//간결한 풀이
func solution2(_ emergency:[Int]) -> [Int] {
    emergency.map { emergency.sorted(by: >).firstIndex(of: $0)!+1 }
}