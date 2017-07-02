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