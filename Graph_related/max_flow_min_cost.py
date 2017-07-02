import sys
import utils
import Bellman_ford
from Max_flow import Max_flow
import os
def read_graph(filename):
	graph = {}
	f = open(filename)
	node_set = {}
	for line in f:
		line = line.strip().split("\t")
		src = int(line[0])
		aim = int(line[1])
		capacity = eval(line[2])
		cost = eval(line[3])
		node_set.setdefault(src, set())
		node_set.setdefault(aim, set())
		node_set[src].add(aim)
		node_set[aim].add(src)
		graph.setdefault(src, {})
		graph[src][aim] = (capacity, 0, cost)
	return graph, node_set
	
def write_mids(vertex_list):#see the middle result of Bellman_ford
	f = open("mids_bellman_ford" , "w")
	for item in vertex_list:
		f.write(str(item.name) + "\t" + str(item.pre) + "\t" + str(item.dis) + "\n")
	f.close()
	
def find_augment_path(graph, src, aim):
	length_graph = {}
	for temp in graph:
		for temp2 in graph[temp]:
			if graph[temp][temp2][0] > graph[temp][temp2][1]: #capacity > flow_now
				length_graph.setdefault(temp, {})
				length_graph[temp][temp2] = graph[temp][temp2][2]
			if graph[temp][temp2][1] > 0:
				#print "neg edge exist"
				length_graph.setdefault(temp2, {})
				length_graph[temp2][temp] = - graph[temp][temp2][2]
	vertex_list, item_index = Bellman_ford.Bellman_ford(length_graph)#calc the min path with Bellman_ford
	#write_mids(vertex_list)
	path = []
	idx1 = utils.search_list(vertex_list, aim)
	idx2 = utils.search_list(vertex_list, src)
	if idx1 == -1 or idx2 == -1:
		print "No edge for src/aim, Finish"
		return False, path
	pre = aim
	while pre != src:
		print pre 
		idx = utils.search_list(vertex_list, pre)
		now = vertex_list[idx].pre
		if now in length_graph and pre in length_graph[now]:
			if length_graph[now][pre] > 0:
				path.append((pre,0))
			else:
				path.append((pre,1))
		pre = now
	path.append((src,0))
	return True,path

def cal_max_flow(graph, src):
	total = 0
	for item in graph[src]:
		total += graph[src][item][1]
	return total
	
def update(graph, path, src, aim, now ,max):
	pre = src
	flow_list = []
	print "Augment path is :"
	print path
	for i in range(len(path) - 2, -1, -1):
		now = path[i][0]
		if path[i][1] == 0:
			flow_list.append(graph[pre][now][0] - graph[pre][now][1])
		if path[i][1] == 1:
			flow_list.append(graph[now][pre][1])
		pre = now
	delta = min(flow_list)
	if delta > max - now:#to control total flow<max_flow, which can extend to find min cost for a certain count of flow
		delta = max - now
	pre = src
	for i in range(len(path) - 2, -1, -1):
		now = path[i][0]
		if path[i][1] == 0:
			temp = graph[pre][now][0]
			temp1 = graph[pre][now][1]
			temp2 = graph[pre][now][2]
			graph[pre][now] = (temp, temp1 + delta, temp2)
		if path[i][1] == 1:
			temp = graph[now][pre][0]
			temp1 = graph[now][pre][1]
			temp2 = graph[now][pre][2]
			graph[now][pre] = (temp, temp1 - delta, temp2)
		pre = now
	return cal_max_flow(graph, src)

def write_flow(graph, output):
	f1 = open(output, "w")
	for item in graph:
		for item2 in graph[item]:
			f1.write(str(item) + "\t" + str(item2) + "\t" + str(graph[item][item2][0]) + "\t" + str(graph[item][item2][1]) + "\t"+ str(graph[item][item2][2]) +"\n" )
	f1.close()
	
def cal_cost(graph):
	total = 0
	for temp in graph:
		for temp2 in graph[temp]:
			total += graph[temp][temp2][2] * graph[temp][temp2][1]
	return total
	
def main_deal(filename, output):
	max_flow = Max_flow(filename)
	print "The max_flow is " + str(max_flow)
	graph, node_set = read_graph(filename)
	src = 0
	aim = len(node_set) - 1
	flow_now = 0
	#max_flow = 10
	while True:
		flag,path = find_augment_path(graph, src, aim)
		if not flag:
			print "No augment path any more. Finish"
			break
		flow_now = update(graph, path, src, aim, flow_now, max_flow)
		if flow_now >= max_flow:
			break
		#os.system('pause')
	write_flow(graph, output)
	return cal_cost(graph)
	
if __name__ == '__main__':
	print "python this.py input_name output_name max_flow"
	total = main_deal(sys.argv[1], sys.argv[2])
	print "The min cost of max flow is :" + str(total)