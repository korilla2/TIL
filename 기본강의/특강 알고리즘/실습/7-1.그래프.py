class Graph():
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


G = None

G = Graph(4)

G.graph[0][1] = 1
G.graph[0][2] = 1
G.graph[0][3] = 1

G.graph[1][0] = 1
G.graph[1][2] = 1
G.graph[1][3] = 1

G.graph[2][0] = 1
G.graph[2][1] = 1
G.graph[2][3] = 1

G.graph[3][0] = 1
G.graph[3][1] = 1
G.graph[3][2] = 1

for i in range(4):
    for j in range(4):
        print(G.graph[i][j], end=' ')
    print()
