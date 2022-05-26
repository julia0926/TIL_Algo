import Foundation

func solution(_ n:Int) -> String
{
    if n >= 0 {
        var numbers = [0,1,1]
        for i in 0...n{
            if i == 0 || i == 1 || i == 2{
                continue
            } else {
                numbers.append(numbers[i-1] + numbers[i-2])
            }
        }
        return String(numbers[n])
    } else {
        let n = -n
        var numbers = [1,-1,2]
        for i in 0...n{
            if i == 0 || i == 1 || i == 2{
                continue
            } else {
                numbers.append(numbers[i-1] - numbers[i-2])
            }
        }
        return String(numbers[n-1])
    }
    
}