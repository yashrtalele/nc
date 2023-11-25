class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes

    def create_graph(self, file_name):
        init_graph = {}
        for node in self.nodes:
            init_graph[node] = {}
        
        with open(file_name, 'r') as file:
            for line in file:
                start, end, cost = line.split()
                cost = int(cost)
                init_graph[start][end] = cost
        return init_graph
    
    def build_graph(self, init_graph):
        graph = {}
        for node in self.nodes:
            graph[node] = {}
        graph.update(init_graph)
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
        return graph
    
    def get_neighbors(self, node, graph):
        neighbors = []
        for out_node in self.nodes:
            if graph[node].get(out_node, False) != False:
                neighbors.append(out_node)
        return neighbors