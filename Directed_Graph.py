class Directed_Graph:
    def __init__(self, number_of_nodes, edges, weighted=False):
        self.number_of_nodes = number_of_nodes
        self.edges = edges
        self.weighted = weighted
       
        self.data = [[] for _ in range(self.number_of_nodes)]
        
        if self.weighted: 
            self.weights = {}
        
        for edge in self.edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weights[node1, node2] = weight
                
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                
        #    print(self.data)
        #    print(self.weights)
               
    def __repr__(self):
        print("Adjaceny list:")
        if self.weighted:
            for node, neighbours in enumerate(self.data):
                result += f"{node} : "
                for neighbour in neighbours:
                    result += f"({neighbour} --> {self.weights[node, neighbour]}) "
                result += "\n"
            return result

        else:
            return "\n".join("{} : {}".format(node, neighbours) for node, neighbours in enumerate(self.data))
        
    def __str__(self):
        return self.__repr__() 

if __name__ == "__main__":
                
#                            3    .   . 4
#                    0 ------------ 1 ------ 7   
#                 /  |                     /.
#             4 /    | 2                / 2
#             /     .|      6     .   /
#          . 8       3 ------------ 2       6   
#             \      |              |     /.
#             8 \    | 1          1 |   / 8
#                 \  |.            .| /
#                  . 4              5
#

    number_of_nodes = 9
    undirect_edges = [(0,1),(0,3),(0,8),(7,1),(3,2),(3,4),(8,4),(2,5),(2,7),(5,6)]
    undirected_g = Directed_Graph(number_of_nodes, undirect_edges)
    print(undirected_g)
    
    
#                               3          
#                    0 -------------------> 1
#                    |  |\-                 | 
#                  4 |        \             | 2
#                    |             \6       | 
#                   \|/                  \  \|/ 
#                    2                      3
#
#    num_nodes = 4
#    directed_edges = [(0,2,4),(0,1,3),(1,3,2),(3,0,6)]
#    directed_g = Directed_Graph(num_nodes, directed_edges, weighted=True)
#    print(directed_g)