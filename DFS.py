def dfs_iterative(graph, start):
    stack = [start] #start
    path = [] #empty
    # print(stack[0])

    while stack: #stack is not empty
        vertex = stack.pop() #get first node to vertex 
        if vertex in path: #node already in path
            continue #skip
        path.append(vertex) #start adding node to path
        for neighbor in graph[vertex]: #start exploring other node
            stack.append(neighbor) #add neighbor node to stack

    return path


adjacency_matrix = {'A': ['B', 'C','D'], 'B': ['E','F'],'C':['G','H'],'D':['I'],'E':['j','k'],'F':[],
                    'G':['L'], 'H': [], 'I': ['M'],
                    'j': [], 'k': ['N'],'L':[],'M':[],'N':[]}

print(dfs_iterative(adjacency_matrix,'A'))
