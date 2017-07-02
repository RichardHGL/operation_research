import sys

def read_graph(filename):
	graph = {}
	f = open(filename)
	node_set = {}
	for line in f:
		line = line.strip().split("\t")
		src = int(line[0])
		aim = int(line[1])
		capacity = int(line[2])		
		node_set.setdefault(src, set())
		node_set.setdefault(aim, set())
		node_set[src].add(aim)
		node_set[aim].add(src)
		graph.setdefault(src, {})
		graph[src][aim] = (capacity, 0)
	return graph, node_set

def check(item, path):
	for x in path:
		if x[0] == item:
			return True
	return False
	
def find_augment_path_2(path, graph, node_set, src, aim):
	flag = False
	for item in node_set[src]:
		if check(item, path):#to avoid circle
			continue
		if item in graph[src] and graph[src][item][0] > graph[src][item][1]:
			if item == aim:#recusion end
				path.append((aim,0))
				#print "reach aim"
				return True
			else:#continue to deep recusion
				path.append((item,0))
				#print "pos_way"
				#print item
				flag = find_augment_path_2(path, graph, node_set, item, aim)
				if flag:
					break
				else:
					path.pop()
		if item in graph and src in graph[item] and graph[item][src][1] > 0:
			#print "neg_way"
			path.append((item,1))
			#print item
			#back_edge in a path
			flag = find_augment_path_2(path, graph, node_set, item, aim)
			if flag:
				break
			else:
				path.pop()
	return flag
	
def update(graph, path, src, aim):
	pre = src
	flow_list = []
	print "Augment path is :"
	print path
	for i in range(1, len(path)):
		now = path[i][0]
		if path[i][1] == 0:
			flow_list.append(graph[pre][now][0] - graph[pre][now][1])
		if path[i][1] == 1:
			flow_list.append(graph[now][pre][1])
		pre = now
	
	delta = min(flow_list)
	
	pre = src
	for i in range(1, len(path)):
		now = path[i][0]
		if path[i][1] == 0:
			temp = graph[pre][now][0]
			temp1 = graph[pre][now][1]
			graph[pre][now] = (temp, temp1 + delta)
			#graph[pre][now][1] += delta
		if path[i][1] == 1:
			temp = graph[now][pre][0]
			temp1 = graph[now][pre][1]
			graph[now][pre] = (temp, temp1 - delta)
			#graph[pre][now][1] -= delta
		pre = now
	
def write_flow(graph, output):
	f1 = open(output, "w")
	for item in graph:
		for item2 in graph[item]:
			f1.write(str(item) + "\t" + str(item2) + "\t" + str(graph[item][item2][0]) + "\t" + str(graph[item][item2][1]) + "\n" )
	f1.close()
	
def cal_max_flow(graph, src):
	total = 0
	for item in graph[src]:
		total += graph[src][item][1]
	return total
	
def Max_flow(filename):#For out_use of calc of max_flow
	graph, node_set = read_graph(filename)
	src = 0
	aim = len(node_set) - 1
	while True:
		path = []
		path.append((src,0))
		flag = find_augment_path_2(path, graph, node_set, src, aim)
		if not flag:
			print "No augment path any more. Finish"
			break
		'''
		if len(path) == 0 or path[len(path) - 1][0] != aim:
			print "No augment path any more. Finish"
			break
		'''
		update(graph, path, src, aim)
	return cal_max_flow(graph, src)
	
def main_deal(filename, output):
	graph, node_set = read_graph(filename)
	src = 0
	aim = len(node_set) - 1
	while True:
		path = []
		path.append((src,0))
		flag = find_augment_path_2(path, graph, node_set, src, aim)
		if not flag:
			print "No augment path any more. Finish"
			break
		'''
		if len(path) == 0 or path[len(path) - 1][0] != aim:
			print "No augment path any more. Finish"
			break
		'''
		update(graph, path, src, aim)
	write_flow(graph, output)
	return cal_max_flow(graph, src)
		
if __name__ == '__main__':
	print "usage python Max_flow.py input_file output_file"
	total = main_deal(sys.argv[1], sys.argv[2])
	print "MAX_FLOW in this graph is " + str(total)	