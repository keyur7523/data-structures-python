class Weighted_Graph:
    def __init__(self, number_of_nodes, edges, weighted=False, directed=False):
        self.number_of_nodes = number_of_nodes
        self.edges = edges
        self.weighted = weighted
        self.directed = directed
        
        self.data = [[] for _ in range(self.number_of_nodes)]
        self.weights = {}
        
        for edge in self.edges:
            node1, node2, weight = edge
           
            if self.directed:
                self.data[node1].append(node2)
                self.weights[node1, node2] = weight
                
            else:
                self.data[node1].append(node2)
                self.data[node2].append(node1)
                self.weights[node1, node2] =  weight
                self.weights[node2, node1] = weight
               
        #    print(self.data)
        #    print(self.weights)
               
    def __repr__(self):
        result = "Adjaceny list:\n"
        for node, neighbours in enumerate(self.data):
            result += f"{node} : "
            for neighbour in neighbours:
                result += f"({neighbour} --> {self.weights[node, neighbour]}) "
            result += "\n"
        return result
        
    def __str__(self):
        return self.__repr__() 

if __name__ == "__main__":
                
#                            3           4
#                    0 ------------ 1 ------ 7   
#                 /  |                     /
#             4 /    | 2                 / 2
#             /      |      6          /
#           8        3 ------------ 2       6   
#             \      |              |     /
#             8 \    | 1          1 |   / 8
#                 \  |              | /
#                    4              5
#

#    number_of_nodes = 9
#    undirect_edges = [(0,1,3),(0,3,2),(0,8,4),(1,7,4),(2,3,6),(3,4,1),(4,8,8),(2,5,1),(2,7,2),(5,6,8)]
#    undirected_g = Weighted_Graph(number_of_nodes, undirect_edges, weighted=True)
#    print(undirected_g)
    
    
#                               3          
#                    0 -------------------> 1
#                    |  |\-                 | 
#                  4 |        \             | 2
#                    |             \6       | 
#                   \|/                  \  \|/ 
#                    2                      3
#
    num_nodes = 4
    directed_edges = [(0,2,4),(0,1,3),(1,3,2),(3,0,6)]
    directed_g = Weighted_Graph(num_nodes, directed_edges, weighted=True, directed=True)
    print(directed_g)