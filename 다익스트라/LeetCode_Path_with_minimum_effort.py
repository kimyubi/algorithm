class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        Q = [(0,0,0)]        #(diff,x,y)

        r = len(heights)     # r: number of row, c: number of column
        c = len(heights[0])

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        
        result = sys.maxsize # a route's minimum effort
        visited = set()
    
        while Q:
            diff,x,y = heapq.heappop(Q)
    
            if x == r-1 and y == c-1:
                result = min(result,diff)
                    
            visited.add((x,y))
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                    
                if 0 <= nx < r and 0 <= ny < c and (nx,ny) not in visited:
                    alt = abs(heights[x][y] - heights[nx][ny])
                    heapq.heappush(Q, (alt,nx,ny))
                    
        
        return result
            
        
    
        # visited로 방문한 좌표 처리하지 않으면 무한 순회/ 방문한 좌표 처리하면 다른 길로 탐색할 때 탐색에 제약이 있어 최소 effort가 구해지지 않음.

