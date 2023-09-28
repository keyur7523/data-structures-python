class Graph:
    def __init__(self, number_of_nodes, edges):
        self.number_of_nodes = number_of_nodes
        self.data = [[] for _ in range(number_of_nodes)]  # adjaceny list for the nodes of graph
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
        print(self.data)
        
    def __repr__(self):
        return "\n".join("{} : {}".format(node, neighbours) for node, neighbours in enumerate(self.data))
        
    def __str__(self):
        return self.__repr__()
        
    def print_graph_adjacency(self):
        for x in enumerate(self.data):
            print(x)
            
    def adding_edge(self, edges_to_be_added):
        for n1, n2 in edges_to_be_added:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    
    def removing_edge(self, edges_to_be_removed):
        for n1, n2 in edges_to_be_removed:
            self.data[n1].remove(n2)
            self.data[n2].remove(n1)
            
    def adjancency_matrix(self):
        print('   ', end='')
        for n in range(self.number_of_nodes):
            print(f"  {n}", end = "  ")
        print('\n')
        for n1 in range(self.number_of_nodes):
            print(n1, end="  ")
            for n2 in range(self.number_of_nodes):
                if n2 in self.data[n1]:
                    print('  1', end ="  ")
                else: print('  0', end ="  ")
            print('\n')
       
    def bfs(self, root):                                # bfs
        queue = []
        visited = [False] * self.number_of_nodes
        distance = {}
        parent = {}
        visited[root] = True                            # first root in the queue
        queue.append(root)
        idx = 0
        distance[root] = 0
        parent[root] = root
       
        while idx < len(queue):
            current = queue[idx]                        #dequeue
            idx += 1
        
            for node in self.data[current]:
                if node not in queue:                   # adding neighbours in the list of queue
                    queue.append(node)
                    visited[node] = True
                    distance[node] = 1 + distance[current]
                    parent[node] = current
            
        return queue, parent, distance
    
    def dfs(self, root):                                # dfs
        stack = []
        dfs_result = []
        parent = {}
        visited = [False] * self.number_of_nodes
        stack.append(root)
        parent[root] = root
        
        while len(stack) > 0:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                dfs_result.append(current)
                for node in self.data[current]:
                    if not visited[node]:
                        stack.append(node)
                        parent[node] = current
                        
        return dfs_result, parent
           
    def check_all_nodes_connectivity(self):
        if self.number_of_nodes == len(self.bfs(self.data[0][0])[0]):
            return True
        else:
            return False
        
    def connected_nodes(self):
        connected_nodes_list = {}
        for i in range(self.number_of_nodes):
            connected_nodes_list[i] = [x for x in self.bfs(i)[0][1:]]
        return connected_nodes_list
    
    def detect_cycle(self):
        test, count = False, 0
        stack, dfs_list = [0], []
        visited = [False] * self.number_of_nodes
        visited[0] = True
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                dfs_list.append(current)
                for node in self.data[current]:
                    if not visited[node]:
                        stack.append(node)
            else:
                test = True
                count += 1   
        return test, count
       
if __name__ == '__main__':
    
#   0----3                   # Adding edge (0,2)
#   |   /| \                 # Removing edges (1,3) and (2,4)
#   | /  |  \
#   1----2---4 

    num_nodes = 5
    edges = [(0,1), (1,2), (1,3), (0,3), (2,3), (2,4), (3,4)]
    g = Graph(num_nodes, edges)
    print(g)
    print(f"Cyclic: {g.detect_cycle()[0]} number of cycles: {g.detect_cycle()[1]}")
#    g.print_graph_adjacency()
#    print(g)
#    edges_to_be_added = [(0,2)]
#    g.adding_edge(edges_to_be_added)
#    print('\n')
#    print(g)
#    print('\n')
#    edges_to_be_removed = [(1,3), (2,4)]
#    g.removing_edge(edges_to_be_removed)
#    print(g)
#    print('\n')
    
    # g.adjancency_matrix()
    
    # root_for_BFS = 0
    # bfs_list, parent, distance = g.bfs(root_for_BFS)
    
    # print(f"The BFS for root {root_for_BFS} is {bfs_list}. \nThe parents of the nodes in BFS (node:parent) : {parent}. \n The distance from the root node (node:distance) : {distance}.")
    
    # check_var = g.check_all_nodes_connectivity()
    
    # print(f"Are all the nodes connected in this graph: {check_var}.")
    
    # connected_n = g.connected_nodes()   
    # print(f"The connected nodes list: {connected_n}.")
    
    # root_for_DFS = 0
    # dfs_result, parent_list = g.dfs(root_for_DFS)
    
    # print(f"DFS: {dfs_result}")
    
    # print(f"The DFS parent list (node: parent) is: {parent_list}")
   
    # graph2 = Graph(9, [(0,1),(0,3),(1,2),(2,3),(4,5),(4,6),(5,6),(7,8),])
   
    #check_var_2 = graph2.check_all_nodes_connectivity()
    
    #print(f"Are all the nodes connected in this graph: {check_var_2}.")
    
    # connected_n2 = graph2.connected_nodes()   
    # root_for_DFS2 =2
    # print(f"The connected nodes list: {connected_n2}.\nDFS: {graph2.dfs(root_for_DFS2)[0]} \nparent list: {graph2.dfs(root_for_DFS2)[1]}")
    
    cyclic_graph1 = Graph(5, [(1,2), (1,0), (2,0), (0,3), (3,4)])
    print(f"IS graph cyclic: {cyclic_graph1.detect_cycle()[0]} \nThe number of cycles in graph are {cyclic_graph1.detect_cycle()[1]}")