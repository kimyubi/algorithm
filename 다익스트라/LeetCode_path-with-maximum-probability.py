class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        visited = set()
        
        # generate graph
        for (x,y),prob in zip(edges,succProb):
            graph[x].append((y,prob))
            graph[y].append((x,prob))
 
        Q = [(0,1,start)] # (dumy,probability,node)
        
        while Q:
            dumy,probability,node = heapq.heappop(Q)
            visited.add(node)
            
            if node == end:
                return probability
            
            for v,w in graph[node]:
                if v not in visited:
                    alt = probability * w
                    heapq.heappush(Q,(-alt,alt,v))
        
        return 0