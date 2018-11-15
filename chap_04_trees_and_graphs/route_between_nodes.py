from Graph import Graph

def route_between_nodes(tree, start_node, end_node):
        if start_node == end_node:
            return True

        queue = [start_node]
        
        visited = [False] * len(tree.nodes)
        visited[start_node.id] = True

        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.pop()

                if node.id == end_node.id:
                    return True

                visited[node.id] = True
                
                for child in node.children:
                    queue.insert(0, child)
        return False

G = Graph()

a = G.createNode(5)
b = G.createNode(8)
c = G.createNode(6)
d = G.createNode(9)
e = G.createNode(10)

G.addEdge(a, b)
G.addEdge(a, b) # shouldn't work
G.addEdge(a, c)
G.addEdge(b, a)
G.addEdge(b, e)
G.addEdge(e, d)

G.printGraph()

print "There is " + ("" if route_between_nodes(G, a, d) else "not ") + "a route between nodes a and d"