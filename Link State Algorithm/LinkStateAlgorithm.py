from heapq import heapify, heappush
from graph import Graph
from dijkstra import Dijkstra

class LinkStateAlgorithm:
    def __init__(self, nodes):
        self.nodes = nodes

    def build_topology(self, gph, init_graph):
        graph = gph.build_graph(init_graph)
        return graph

    def calculate_shortest_path(self, gph, graph, source, destination):
        dj = Dijkstra()
        previous_nodes, shortest_path = dj.dijkstra(gph = gph, graph = graph, nodes = self.nodes, start_node = source)
        dj.print_result(previous_nodes, shortest_path, start_node=source, target_node=destination)

def main():
    file_name = "test_linkstate.txt"
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    start = 'A'
    end = 'I'
    lsr = LinkStateAlgorithm(nodes)
    gph = Graph(nodes)
    init_graph = gph.create_graph(file_name)
    graph = lsr.build_topology(gph, init_graph)
    lsr.calculate_shortest_path(gph, graph, start, end)

if __name__ == '__main__':
    main()