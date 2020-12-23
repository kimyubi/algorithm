class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        
        for x,y in zip(edges,succProb): # generate graph => start_v : (dst, probability)
            graph[x[0]].append((x[1],float(y)))  
 
            
        Q = [(0,1,start)] # (dumy, probability, node)
        # dumy는 probability가 큰 값을 우선 순위로 설정하기 위한 기준으로 쓰레기 값이다.
        
        while Q:
            dumy,probability,node = heapq.heappop(Q)
            
            if node == end:
                return float(probability)
            
            for v,w in graph[node]:
                alt = float(probability * w)
                heapq.heappush(Q,(-alt,alt,v))  # probability가 큰 것을 우선
                print(Q)
        
        
        return float(0)
                
# 테케 통과 / 제출 실패 - undirected weighted graph가 정점 간 양방향 이동 가능한 그래프인데 단방향 그래프처럼 풀었다.
# 그럼 역방향도 그래프에 추가..? 양방향 무한 순회 문제 생각해보기.       
            
            