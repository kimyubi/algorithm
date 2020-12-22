import sys
from collections import defaultdict
import heapq

graph = defaultdict(list)                        # graph
graph_rev = defaultdict(list)                    # reversed graph
n,m,x = map(int,sys.stdin.readline().split())    # n : number of students, m : number of edges, x :  party place

# generate graph
for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().split())  # u: source vertex, v: destination vertex, w: weight
    graph[u].append((v,w))
    graph_rev[v].append((u,w))


#dijxtra algorithm
def dijxtra(start_v , graph):
    results = defaultdict(int)                    # Shortest distance to each vertex
    Q = [(0,start_v)]                             # (time , vertex)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in results:
            results[node] = time
            for v,w in graph[node]:
                alt = time + w
                heapq.heappush(Q,(alt,v))

    return results


results = dijxtra(x,graph)
rev_results = dijxtra(x,graph_rev)

solution = []
for i in range(1,n+1):
    if i == x:
        # always 0 
        continue

    solution.append(results[i] + rev_results[i])

print(max(solution))



