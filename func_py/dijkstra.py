from collections import defaultdict
import heapq as heap

def dijkstra(G, startingNode):
    visited = set()
    parentsMap = {}
    pq = []
    nodeCosts = defaultdict(lambda: float('inf'))
    nodeCosts[startingNode] = 0
    heap.heapppush(pq, (startingNode))

    while pq:
        _, node = heap.heappop(pq)
        visited.add(node)

        for adjNode, weight in G[node].items():
            if adjNode in visited: continue

            newCost = nonodeCosts[node] + weight
            if nodeCosts[adjNode] > newCost:
                parentsmap[adjNode] = node
                nodeCosts[adjNode] = newCost
                heap.heappush(pq, (newCost, adjNode))

    return parentsMap, nodeCosts