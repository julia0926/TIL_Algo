import Foundation

func solution(_ video_len:String, _ pos:String, _ op_start:String, _ op_end:String, _ commands:[String]) -> String {
    
    func calculateTime(timeString: String) -> Int {
        let timeComponents = timeString.components(separatedBy: ":").compactMap { Int($0) }
        let (minute, second) = (timeComponents[0], timeComponents[1])
        let timeInSecond = minute * 60 + second
        return timeInSecond
    }
    
    func secondToTime(totalSecond: Int) -> String {
        let minute = totalSecond / 60
        let second = totalSecond % 60
        return String(format: "%02d:%02d", minute, second)
    }
    
    let videoSecond = calculateTime(timeString: video_len)
    let (openingStart, openingEnd) = (calculateTime(timeString: op_start), calculateTime(timeString: op_end))
    let openingRange = openingStart..<openingEnd  // 오프닝 끝 시점은 미포함 (문제 조건 명시적이라면 ..< 유지)
    var posInSecond = calculateTime(timeString: pos)
    
    // 초기 위치가 오프닝에 포함될 경우, 오프닝 끝으로 이동
    if openingRange.contains(posInSecond) {
        posInSecond = openingEnd
    }
    
    for command in commands {
        if command == "next" {
            posInSecond = min(posInSecond + 10, videoSecond)
        } else if command == "prev" {
            posInSecond = max(posInSecond - 10, 0)
        }
        if openingRange.contains(posInSecond) {
            posInSecond = openingEnd
        }
//        print(command, posInSecond)
    }
    
    let result = secondToTime(totalSecond: posInSecond)
//    print(result)
    return result
}