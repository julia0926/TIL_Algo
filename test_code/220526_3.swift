//이 문제는 오답임 !

import Foundation

func calculate(_ s: String, one: Int, two: Int) -> Int {
    switch s {
    case "*":
        return one * two
    case "+":
        return one + two
    case "-":
        return one - two
    default:
        return one / two
    }
}

func solution(_ p:[String]) -> Int64 {
    var p = p
    var sum = 0
    var idx = 0
    while p.count != 1 {
        if Int(p[idx]) == nil { //숫자가 아니라면
            sum = calculate(p[idx], one: Int(p[idx-2])!, two: Int(p[idx-1])!)
            p.insert("\(sum)", at: idx+1)
            p.removeSubrange(idx-2...idx)
            idx = 0
        } else {
            idx += 1
        }
    }
    return Int64(sum)
}

print(solution(["12","2","5","+","*","9","3","/","-"]))
print(solution(["1","1","+","1","1","+","*"]))