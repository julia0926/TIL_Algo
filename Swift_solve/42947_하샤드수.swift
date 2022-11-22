//https://school.programmers.co.kr/learn/courses/30/lessons/12947/solution_groups?language=swift

func solution(_ x:Int) -> Bool {
    let div = String(x).map { Int(String($0))! }.reduce(0, +)
    return x % div == 0 ? true : false
}