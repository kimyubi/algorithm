from collections import defaultdict
import sys
import heapq
dist = defaultdict(int)                 # Shortest route to each point
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


#dijxstra
def dijx(cnt, n, graph):
    Q = [(graph[0][0], 0, 0)]            # (wegiht, x, y)
    visited = set()                      

    while Q:
        w, x, y = heapq.heappop(Q)
      
        #### ~ 시간 초과 해결한 코드
        
        if x == n-1 and y == n-1:       
            print("Problem {0}: {1}".format(cnt, w))
            break
        
         # 이미 방문한 좌표는 탐색 x
        if (x,y) in visited:
            continue
        
         # 현재 좌표 방문 처리
        visited.add((x,y)) 
        
        ####

        # 시작점 (0,0)부터 현재 좌표까지의 최단 거리를 저장하는 딕셔너리 : dist
        # 가장 처음 현재 좌표(x,y)를 키로 하여 저장된 값이 최단 거리이므로, 현재 좌표를 키 값으로 하는 값이 이미 있으면 무시한다.
        if (x, y) not in dist:
            dist[(x, y)] = w

        # 동서남북 탐색
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
    
            if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
                nw = w + graph[nx][ny]
                heapq.heappush(Q,(nw, nx, ny))
    

cnt = 1
while True:
    N = int(input())
    if N == 0:
        break

    graph = [[int(x) for x in input().split()] for y in range(N)]
    dijx(cnt, N, graph)
    cnt += 1


