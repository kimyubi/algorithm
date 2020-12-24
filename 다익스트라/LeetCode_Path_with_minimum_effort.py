class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        Q = [(0,0,0)]  #(diff,x,y)
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        
        dist = collections.defaultdict(int)
        n = len(heights)
        
        dist[(n-1,n-1)] = sys.maxsize
        visited = set()
    
        while Q:
            diff,x,y = heapq.heappop(Q)
    
            if x == n-1 and y == n-1:
                if diff < dist[(n-1,n-1)]:
                    dist[(n-1,n-1)]= diff
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                visited.add((x,y))
                
                if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
                    alt = abs(diff - heights[nx][ny])
                    heapq.heappush(Q, (alt,nx,ny))
                    
        
        return dist[(n-1, n-1)]
        
    
        # visited로 방문한 좌표 처리하지 않으면 무한 순회/ 방문한 좌표 처리하면 다른 길로 탐색할 때 탐색에 제약이 있어 최소 effort가 구해지지 않음.
        
            
            