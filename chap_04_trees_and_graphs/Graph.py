class Node:
    def __init__(self, value, id):
        self.value = value
        self.id = id
        self.children = []

class Graph:
    def __init__(self):
        self.nodes = []
    
    def createNode(self, value):
        new_node = Node(value, len(self.nodes))
        self.nodes.append(new_node)
        return new_node
    
    def addEdge(self, node1, node2):
        node1_children = self.nodes[node1.id].children
        if node2 not in node1_children:
            self.nodes[node1.id].children.append(node2)
    
    def printGraph(self):
        print "GRAPH:"
        for node in self.nodes:
            print str(node.id) + " (" + str(node.value) + ")", "->", [str(child.id) + " (" + str(child.value) + ")" for child in node.children]
        print "-------"

    def breadthFirstSearch(self, start_node, end_node):
        if start_node == end_node:
            return True

        queue = [start_node]
        
        visited = [False] * len(self.nodes)
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

print G.breadthFirstSearch(a, d)
