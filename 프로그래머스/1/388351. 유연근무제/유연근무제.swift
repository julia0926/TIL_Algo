import Foundation

func solution(_ schedules:[Int], _ timelogs:[[Int]], _ startday:Int) -> Int {
    // 60 넘어가면 +1 처리
    var lateCount = schedules.count
  let allowedArrivalTime = schedules.map { (time: Int) -> Int in
    var hour = (time + 10) / 100
    var minute = (time + 10) % 100
    if minute >= 60 {
        hour += 1
        minute -= 60
    }
    return hour * 100 + minute
}
    
    // 지각 체크
    for (member, weekTimeLog) in timelogs.enumerated() { // 한명씩 돌아가면서 일주일치 출근 체크
        var startDay = startday
        let targetTime = allowedArrivalTime[member] // 목표 시간
        // 일주일 지각 했나 체크
//        print("-----\(member)-----")
        for time in weekTimeLog {
            if startDay > 7 { startDay -= 7 }
            if (1...5).contains(startDay) {
                if targetTime < time { // 한번이라도 지각 했다면
                    lateCount -= 1
//                    print("지각!! 😤", targetTime, time)
                    break
                }
            }
            startDay += 1
        }
        startDay = startday
    }
    return lateCount
}
