//
//  main.swift
//  Algorithm
//
//  Created by Julia on 2022/12/30.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0] //정점
let m = input[1] //간선
let v = input[2] //시작정점

var visited = Array(repeating: false, count: n+1)
var graph = Array(repeating: Array(repeating: 0, count: n+1), count: n+1)

//양방향 연결
for _ in 0..<m {
    let nums = readLine()!.split(separator: " ").map { Int(String($0))! }
    graph[nums[0]][nums[1]] = 1
    graph[nums[1]][nums[0]] = 1
}

func dfs(_ v: Int) {
    visited[v] = true
    print(v, terminator: " ")
    for i in 1..<n+1 {
        if visited[i] == false && graph[v][i] == 1 {
            dfs(i)
        }
    }
}

func bfs(_ v: Int) {
    var queue: [Int] = []
    visited[v] = false
    queue.append(v)
    while !queue.isEmpty {
        var val = queue.removeLast() //pop
        print(val, terminator: " ")
        for i in 1..<n+1 {
            if visited[i] == true && graph[val][i] == 1 {
                queue.append(i)
                visited[i] = false
            }
        }
    }
}

dfs(v)
print()
bfs(v)


