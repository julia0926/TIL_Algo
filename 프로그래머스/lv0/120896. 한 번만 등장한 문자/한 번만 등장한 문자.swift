import Foundation


func solution(_ s:String) -> String {
    var dic: [String: Int] = [:]
    let arr: [String] = s.map { String($0) }
    for a in arr {
        if dic[a] == nil {
            dic[a] = 1
        } else {
            dic[a]! += 1
        }
    }
    let result = dic.filter { $0.value == 1 }.map { $0.key }.sorted().joined()
    return result
}