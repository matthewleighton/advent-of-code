graph = {
    'A': ['start', 'c', 'b', 'end'],
    'b': ['start', 'A', 'd', 'end'],
    'c': ['A'],
    'd': ['b'],
    'end': ['A', 'b'],
    'start': ['A', 'b']
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

all_routes = []

def bfs(visited, graph, node):
	visited.append(node)
	queue.append(node)

	while queue:
		current_location = queue.pop(0) 
		# print(current_location, end = " ") 

		for neighbour in graph[current_location]:
			if neighbour not in visited:

				if neighbour.islower():
					visited.append(neighbour)

				queue.append(neighbour)

				

				print(queue)

# Driver Code
bfs(visited, graph, 'start')