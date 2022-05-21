import Foundation

func solution(_ answers:[Int]) -> [Int] {
    var one = [1,2,3,4,5]
    var two = [2,1,2,3,2,4,2,5]
    var three = [3,3,1,1,2,2,4,4,5,5]
    var score = [0, 0, 0]
    
    for idx in 0..<answers.count {
        if one[idx%5] == answers[idx] { score[0] += 1 }
        if two[idx%8] == answers[idx] {  score[1] += 1 }
        if three[idx%10] == answers[idx]{ score[2] += 1 }
    }
    var answer = [Int]()
    let maxValue = score.max() ?? 0
    for (idx, s) in score.enumerated() {
        if maxValue == s {
            answer.append(idx+1)
        }
    }
    return answer
}

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
