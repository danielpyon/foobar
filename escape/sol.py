from collections import deque
import numpy as np

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
    def bfs(self, s, t, path):
        q = deque()
        q.append(s)
        visited = [False] * self.n
        visited[s] = True
        while q:
            node = q.popleft()
            neighbors = self.graph[node]
            for i, adj in enumerate(neighbors):
                if adj > 0 and not visited[i]:
                    q.append(i)
                    visited[i] = True
                    path[i] = node
        return visited[t]
    def max_flow(self, source, sink):
        flow = 0
        path = [-1] * self.n
        while self.bfs(source, sink, path):
            dflow = float('inf')
            s = sink
            while s != source:
                dflow = min(dflow, self.graph[path[s]][s])
                s = path[s]
            flow += dflow
            v = sink
            while v != source:
                u = path[v]
                self.graph[u][v] -= dflow
                self.graph[v][u] += dflow
                v = path[v]
        return flow

def solution(entrances, exits, path):
    s, t = len(path) - 1, len(path)
    path = np.pad(np.array(path, dtype=float), (0, 2), 'constant')
    path[s, entrances] = float('inf')
    path[exits, t] = float('inf')
    path = path.tolist()
    
    g = Graph(path)
    return g.max_flow(s, t)

print solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
print solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])

