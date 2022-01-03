import heapq
import sys
input= sys.stdin.readline
INF = 1e9
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for tc in range(int(input())):
    n = int(input())
    board = []
    for _ in range(n) :
        board.append(list(map(int,input().split())))
    distance = [[INF] * n for _ in range(n)]
    x,y = 0,0
    distance[x][y] = board[x][y]
    q = [(distance[x][y],x,y)]

    while q:
        dist,x,y = heapq.heappop(q)
        if distance[x][y] < dist :
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n :
                cost = dist + board[nx][ny]
                if distance[nx][ny] > cost :
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost,nx,ny))
    print(distance[n-1][n-1])

"""
testcase
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4

answer : 20 19 36
"""