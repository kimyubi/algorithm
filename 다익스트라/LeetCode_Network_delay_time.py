class Solution:
    # u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
    # There are N network nodes, labelled 1 to N / times[i] = (u, v, w) /  k = start_vertex
    
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list) 
        dist = collections.defaultdict(int)    # Shortest route to each point
        
        for u,v,w in times:
            graph[u].append([v,w])
            
        
        Q = [(0,K)]   # [(time,node)]
        
        while Q:
            time, node = heapq.heappop(Q)
            
            if node not in dist:
                dist[node] = time
                
                for v,w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q,(alt,v))
            
        
        if len(dist) != N:
            return -1
        
        return max(dist.values())
            
        
