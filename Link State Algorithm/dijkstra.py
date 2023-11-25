from sys import maxsize

class Dijkstra:
    def dijkstra(self, gph, graph, nodes, start_node):
        unvisited_nodes = nodes
        shortest_path = {}
        prev_node = {}
        for node in unvisited_nodes:
            shortest_path[node] = maxsize
        shortest_path[start_node] = 0
        while unvisited_nodes:
            curr_min = None
            for node in unvisited_nodes:
                if curr_min == None:
                    curr_min = node
                elif shortest_path[node] < shortest_path[curr_min]:
                    curr_min = node
            neighbors = gph.get_neighbors(curr_min, graph)
            for neighbor in neighbors:
                temp = shortest_path[curr_min] + graph[curr_min][neighbor]
                if temp < shortest_path[neighbor]:
                    shortest_path[neighbor] = temp
                    prev_node[neighbor] = curr_min
            unvisited_nodes.remove(curr_min)
        return prev_node, shortest_path

    def print_path(self, prev_node, shortest_path, start_node, target_node):
        path = []
        node = target_node
        while node != start_node:
            path.append(node)
            node = prev_node[node]
        path.append(start_node)
        print("Shortest Path Distance = {}.".format(shortest_path[target_node]))
        print("Shortest Path = ", end="")
        print(" -> ".join(reversed(path)))