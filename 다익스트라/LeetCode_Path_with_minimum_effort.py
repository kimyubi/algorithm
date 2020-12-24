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


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0

        r, c = len(heights), len(heights[0])
        heap = [(0,0,0)]
        res = 0
        visited = set()
	
        while heap:
            # Always pop up the smaller abs distance 
            d, x, y = heapq.heappop(heap)

            res = max(res, d)
            if (x, y) == (r-1, c-1):
                return res
            visited.add((x, y))
        
            for nx, ny in (x+1, y), (x-1,y), (x, y+1), (x, y-1):
                if nx >= 0 and nx < r and ny >= 0 and ny < c and (nx, ny) not in visited:
                    nd = abs(heights[nx][ny] - heights[x][y])
                    heapq.heappush(heap, (nd, nx, ny))

        return res
        