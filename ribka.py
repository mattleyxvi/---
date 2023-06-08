from operator import index


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)


    def searching_algo(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False


    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow


            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


letters = ['source','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
f = open('input_s1_11.txt')

num = int(f.readline())
graph = []
words = []
for i in range(54):
    Temp = [0] * 54
    graph.append(Temp)
for i in range(num):
    words.append(f.readline())
for i in range(int(f.readline())):
    a = f.readline().split(' ')
    graph[0][letters.index(a[0])]=int(a[1])
for i in range(int(f.readline())):
    a= f.readline().split(' ')
    graph[letters.index(a[0])+26][53]=int(a[1])
for word in words:
    graph[letters.index(word[0])][letters.index(word[-2])+26]+=1


g = Graph(graph)

source = 0
sink = 53   

print("Max words: %d " % g.ford_fulkerson(source, sink))