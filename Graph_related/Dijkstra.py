import sys
import random

class vertex(object):
	dis = 0
	pre = -1
	name = -1
	def __init__(self, name):
		self.name = name
		self.set_dis(-1)
		self.set_pre(-1)
		
	def set_dis(self,dis):
		self.dis = dis
		
	def set_pre(self, pre):
		self.pre = pre

def search_list(vertex_list, name):
	for i in range(0, len(vertex_list)):
		if vertex_list[i].name == name:
			return i
	return -1
	
def search_min(vertex_list):
	min_dis = 100000
	min_place = -1
	for i in range(0, len(vertex_list)):
		if vertex_list[i].dis > 0 and vertex_list[i].dis < min_dis:
			min_dis = vertex_list[i].dis
			min_place = i
	return min_place
	
def relax(vertex_list, temp_vertex, graph):#relax a node and edge related with it
	for item in vertex_list:
		temp1 = temp_vertex.name
		temp2 = item.name
		if temp2 in graph[temp1]:
			temp_dis = temp_vertex.dis + graph[temp1][temp2]
			if item.dis == -1:
				item.set_dis(temp_dis) 
				item.set_pre(temp1)
			else:
				if item.dis > temp_dis:
					item.set_pre(temp1)
					item.set_dis(temp_dis)
	
def Dijkstra(graph, src):
	vertex_list = []
	done_list = []
	for item in graph:
		ver_temp = vertex(item)
		vertex_list.append(ver_temp)
	idx = search_list(vertex_list, src)
	if idx == -1:
		print "Error, src node not in graph!"
		sys.exit(0)
	done_list.append(vertex_list.pop(idx))
	old_x = 0
	done_list[0].set_dis(0)
	while len(vertex_list) > 0:
		relax(vertex_list, done_list[old_x], graph)
		old_x += 1
		idx = search_min(vertex_list)#find the one who is closet to done_list
		if idx == -1:
			print "Error, min node not in the left vertexes!"
			sys.exit(0)
		done_list.append(vertex_list.pop(idx))
	return done_list
		
def read_graph(filename):
	f = open(filename)
	graph = {}
	for line in f:
		(src, aim, weight) = line.strip().split("\t")
		graph.setdefault(int(src), {})
		graph[int(src)][int(aim)] = eval(weight)
	return graph
	
def write_MST(result, output_file, graph):
	f1 = open(output_file, "w")
	for i in range(1, len(result)):
		f1.write( str(result[i].pre) + "\t" + str(result[i].name) + "\t" + str(graph[result[i].pre][result[i].name]) + "\n")
	f1.close()
	
def find_way(result, src, aim):#get the path from pre recursion
	idx = search_list(result, aim)
	if idx == -1:
		print "aim node not exist"
	pre = aim
	while pre != src:
		print pre 
		idx = search_list(result, pre)
		pre = result[idx].pre
	print src
	print "The best way is found!"
	
def main_deal(input_file, output_file):
	graph = read_graph(input_file)
	result = Dijkstra(graph, 0)
	write_MST(result, output_file, graph)
	find_way(result, 0, 10)
	
if __name__ == '__main__':
	print "usage python Dijkstra.py input_file output_file"
	main_deal(sys.argv[1], sys.argv[2])