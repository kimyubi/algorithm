class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        ### generate Graph
        graph = collections.defaultdict(list)
        
        for u,v,w in flights:
            graph[u].append((v,w))
        ### 
        
        Q = [(0,src,K)]  # (cost,vertex,K)
        
        while Q:
            price,node,k  = heapq.heappop(Q)
            
            if node == dst:
                return price
            
            if k >= 0:
                for v,w in graph[node]:
                    alt = price + w
                    
                    # update number of stops
                    heapq.heappush(Q,(alt ,v, k-1))
        
        return -1
        