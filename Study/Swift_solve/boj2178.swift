//
//  main.swift
//  Algorithm
//
//  Created by Julia on 2022/12/30.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let m = input[1]

var graph = [[Int]]()

for _ in 0..<n {
    graph.append(readLine()!.map { Int(String($0))! })
}

func bfs() {
    var queue: [[Int]] = [[0, 0]]
    
    while !queue.isEmpty {
        let pop = queue.removeFirst()
        let x = pop[0]
        let y = pop[1]
        
        for val in [[0, 1], [0, -1], [1, 0], [-1, 0]] {
            let nx = val[0] + x
            let ny = val[1] + y
            if 0 <= nx && n > nx && 0 <= ny && m > ny && graph[nx][ny] == 1 {
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
            }
        }
    }
}

bfs()
print(graph[n-1][m-1])
