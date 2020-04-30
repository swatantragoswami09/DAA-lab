
import itertools
def floyd_warshall(graph,vertex_num):
	for k in range(vertex_num):
		for i,j in itertools.product(range(vertex_num),range(vertex_num)):
			if graph[i][j] > graph[i][k] + graph[k][j]:
				graph[i][j] = graph[i][k] + graph[k][j]

graph = [[1000 for j in range(4)] for i in range(4)]   #graph with four vertex
for i,j in itertools.product(range(4),range(4)):  
	if i == j:
		graph[i][j] = 0
graph[0][2] = -2
graph[1][0] = 4
graph[1][2] = 3
graph[2][3] = 2
graph[3][1] = -1
for i in range(4):
	print(graph[i])
print()
print('.........After floyd-warshall Algorithm.........')
print()
floyd_warshall(graph,4)
for i in range(4):
	print(graph[i])
