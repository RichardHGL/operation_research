def get_paras(ss):
	#print ss
	length = len(ss)
	spcial_list = ['.', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	vars = []
	paras = []
	minus_flag = False
	number_flag = True
	var_flag = False
	temp_str = ""
	i = 0
	while( i < length):
		if number_flag and ss[i] not in spcial_list:
			if temp_str == "":
				if minus_flag:
					paras.append(-1)
				else:
					paras.append(1)
			else:
				paras.append(eval(temp_str))
			minus_flag = False
			number_flag = False
			var_flag = True
			temp_str = ""
		if var_flag:
			while i < length and ss[i] != '+' and ss[i] != '-':
				temp_str += ss[i]
				i += 1
			vars.append(temp_str)
			temp_str = ""
			number_flag = True
			var_flag = False
		if i >= length:
			break
		if ss[i] == '-':
			minus_flag = True
			number_flag = True
			var_flag = False
		elif ss[i] == '+':
			number_flag = True
			var_flag = False
		elif ss[i] == '(':
			depth = 0
			while( i < length ):# To avoid ()qiantao
				if ss[i] == '(':
					depth += 1
				elif ss[i] == ')':
					depth -= 1
					if depth == 0:
						break
				temp_str += ss[i]
				i += 1
				if i >= length:
					print "Error expresssion !" + ss
					sys.exit(0)
			temp_str += ss[i]
		else :
			temp_str += ss[i]
		i += 1
	if temp_str != "":
		if number_flag:
			vars.append( str(1) )
			paras.append( eval(temp_str) )
		elif var_flag:
			vars.append(temp_str)
	#for i in range(0, len(vars) ):
	#	print vars[i] + "\t" + str(paras[i])
	return vars, paras
	
def pre_deal(filename):
	f = open(filename)
	#var_set = set()
	Mylist = []
	idx = 0
	temp_vars = []
	temp_paras = []
	b = []
	for line in f:
		line = line.strip().replace(" ", "")
		if line == "":
			continue
		idx += 1
		if idx == 1:
			if line.startswith("min"):
				aim_var =  line.split("=")[0][3:]
				temp_vars,temp_paras = get_paras( line.split("=")[1] )
			elif line.startswith("max"):
				aim_var =  line.split("=")[0][3:]
				temp_vars,temp_paras = get_paras( line.split("=")[1] )
		else :
			temp_vars,temp_paras = get_paras( line.split("=")[0] )
			b.append(line.split("=")[1])
		for item in temp_vars:
			#var_set.add(item)
			if item not in Mylist:
				Mylist.append(item)
	for item in b:
		if b < 0:
			print "Error in limit right side!"
			sys.exit(0)
	#return list(var_set)
	f.close()
	return Mylist	
	
def mid_deal(var_set, filename):
	f = open(filename)
	idx = 0
	var_index = {}
	var_para = {}
	for item in var_set:
		var_index[idx] = item
		#var_index[item] = idx
		idx += 1
	idx = 0
	aim_var = ""
	temp_vars = []
	temp_paras = []
	b = []
	for line in f:
		line = line.strip().replace(" ", "")
		if line == "":
			continue
		var_para.setdefault(idx, [])
		if idx == 0:
			if line.startswith("min"):
				aim_var =  line.split("=")[0][3:]
				temp_vars,temp_paras = get_paras( line.split("=")[1] )
				for i in range(0, len(var_index)):
					if var_index[i] in temp_vars:
						var_para[idx].append( float( -temp_paras[temp_vars.index(var_index[i])] ) )
					else :
						var_para[idx].append(0.00)
				#for item in temp_vars:
			elif line.startswith("max"):
				aim_var =  line.split("=")[0][3:]
				temp_vars,temp_paras = get_paras( line.split("=")[1] )
				for i in range(0, len(var_index)):
					if var_index[i] in temp_vars:
						var_para[idx].append( float( temp_paras[temp_vars.index(var_index[i])] ) )
					else :
				#for item in temp_vars:
						var_para[idx].append(0.00)
		else :
			temp_vars,temp_paras = get_paras( line.split("=")[0] )
			b.append(eval(line.split("=")[1]) )
			for i in range(0, len(var_index)):
					if var_index[i] in temp_vars:
						var_para[idx].append( float( temp_paras[temp_vars.index(var_index[i])] ) )
					else :
				#for item in temp_vars:
						var_para[idx].append(0.00)
		idx += 1
	return idx, var_para, b