from collections import defaultdict
import sys
import heapq
dist = defaultdict(int)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijx(cnt, n, graph):
    Q = [(graph[0][0], 0, 0)]
    visited = []

    while Q:
      w, x, y = heapq.heappop(Q)
      visited.append((x,y))
      if (x, y) not in dist:
          dist[(x, y)] = w

      for i in range(4):
          nx = dx[i] + x
          ny = dy[i] + y

          if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
              nw = w + graph[nx][ny]
              heapq.heappush(Q,(nw, nx, ny))

    print("Problem {0}: {1}".format(cnt, dist[(n-1,n-1)]))

cnt = 1
while True:
    N = int(input())

    if N == 0:
        break

    graph = [[int(x) for x in input().split()] for y in range(N)]
    dijx(cnt, N, graph)
    cnt += 1


# 시간 초과 => (0,0)에서 모든 좌표까지의 최단거리를 구한 후 dist엔ㄴ 저장해서 시간 초과가 나는 것 같다. 모든 좌표를 다 구하지 않고 푸는 방법 생각해보기
