import sys
import utils
from utils import vertex
	
def get_v(graph):#return a unique list of vertices
	item_set = set()
	for item in graph:
		item_set.add(item)
		for item2 in graph[item]:
			item_set.add(item2)
	return list(item_set)

def relax_list(graph, vertex_list, item_index):#relax all edges in the graph
	for temp in graph:
		for temp1 in graph[temp]:
			pos1 = item_index[temp]
			pos2 = item_index[temp1]
			temp_dis = vertex_list[pos1].dis + graph[temp][temp1]
			if vertex_list[pos2].pre == -1:
				vertex_list[pos2].set_dis(temp_dis)
				vertex_list[pos2].set_pre(temp)
			else:
				if vertex_list[pos2].dis > temp_dis:
					vertex_list[pos2].dis = temp_dis
					vertex_list[pos2].set_pre(temp)
	
def Bellman_ford(graph):
	item_list = get_v(graph)
	item_index = {}
	vertex_list = []
	for i in range(0, len(item_list)):
		ver_temp = vertex(item_list[i])
		item_index[item_list[i]] = i
		vertex_list.append(ver_temp)
	idx = utils.search_list(vertex_list, 0)
	if idx == -1:
		print "Error, src node not in graph!"
		sys.exit(0)
	vertex_list[idx].set_dis(0)
	for i in range(0, len(item_list) - 1):#relax for |V| - 1 times
		relax_list(graph, vertex_list, item_index)
	for temp in graph:#check if there exists negative weight circle
		for temp1 in graph[temp]:
			pos1 = item_index[temp]
			pos2 = item_index[temp1]
			temp_dis = vertex_list[pos1].dis + graph[temp][temp1]
			if vertex_list[pos2].dis > temp_dis:
				print "Error negative circle exists"
	return vertex_list,item_index