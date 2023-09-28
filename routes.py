class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.route_dict = {}
        
        for start, end in self.edges:
            if start in self.route_dict.keys():
                self.route_dict[start].append(end)
            else:
                self.route_dict[start] = [end]
        
    def get_routes(self, start, end, path=[]):
        path += [start]
        
        if start == end:
            return [path]
        if start not in self.route_dict:
            return []
        
        paths = []
        
        for node in self.route_dict[start]:
            if node not in paths:
                new_paths = self.get_routes(node, end, path)
                for p in new_paths:
                    paths.append(p) 
                    
        return paths
    
    def get_shortest_path(self, start, end, path=[]):
        path += [start]
        
        if start not in self.route_dict:
            return None
        
        if start == end:
            return path
        
        shortest_p = None
        for node in self.route_dict[start]:
            if node not in path:
                new_path = list(path)
                sp = self.get_shortest_path(node, end, new_path)
                if sp:
                    if shortest_p is None or len(sp) < len(shortest_p):
                        shortest_p = sp
        return shortest_p
    
if __name__ == "__main__":
    routes = [
        ('Mumbai', 'Paris'), 
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto')
    ]
   
    route_graph = Graph(routes)
    
    start = "Mumbai"
    end = "New York"
    routes_list = route_graph.get_routes(start, end)
    shortest_route = route_graph.get_shortest_path(start, end)
    print(f"The shortest route is {shortest_route}.")
    
    