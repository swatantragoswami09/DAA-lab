def bfs_iterative(graph, start):
    queue = [start] #start
    path = [] #empty
    # print(stack[0])

    while queue: #stack is not empty
        vertex = queue.pop(0) #get first node to vertex 
        if vertex in path: #node already in path
            continue #skip
        path.append(vertex) #start adding node to path
        for neighbor in graph[vertex]: #start exploring other node
            queue.append(neighbor) #add neighbor node to stack

    return path


adjacency_matrix = {'A': ['B', 'C','D'], 'B': ['E','F'],'C':['G','H'],'D':['I'],'E':['j','k'],'F':[],
                    'G':['L'], 'H': [], 'I': ['M'],
                    'j': [], 'k': ['N'],'L':[],'M':[],'N':[]}

print(bfs_iterative(adjacency_matrix,'A'))
