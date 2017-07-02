import sys
import random

def has_way(item, graph):
	nei_list = []
	nei_list.append(item)
	old_x = 0
	x = 1
	while old_x != x:
		num_add = 0
		for i in range(old_x, x):
			for temp in graph[nei_list[i]]:
				if temp not in nei_list:
					nei_list.append(temp)
					num_add += 1
		if num_add == 0:
			break
		old_x = x
		x += num_add
	if len(nei_list) == len(graph):
		return True
	return False

def check(graph):# check if any vertex in graph has way to other vertices
	for item in graph:
		if not has_way(item, graph):
			return False
	return True

def random_graph(size):#generate random size of edge for every vertex, and the weight is random too
	graph = {}
	for i in range(0, size):
		graph.setdefault(i, {})
	for i in range(0, size):
		edge_num = random.randint(1, size - 1)
		for j in range(0, edge_num):
			another = random.randint(0, size - 1)
			while another == i:
				another = random.randint(0, size - 1)
			weight = random.randint(1, 10)
			if another not in graph[i]:
				graph[i][another] = weight
				graph[another][i] = weight
			else :
				if weight < graph[i][another]:
					graph[i][another] = weight
					graph[another][i] = weight
	return graph

def write_graph(graph,output):
	f = open(output, "w")
	for item in graph:
		for item2 in graph[item]:
			f.write(str(item) + "\t" + str(item2) + "\t" + str(graph[item][item2]) + "\n")
	f.close()
	
def get_connected_graph(size, output):
	graph = {}
	while(True):
		graph = random_graph(size)
		if(check(graph)):
			write_graph(graph,output)
			break
	print "Connected Graph is generated!"
	
if __name__ == '__main__':
	print "usage python random_graph.py size output"
	get_connected_graph(eval(sys.argv[1]), sys.argv[2])