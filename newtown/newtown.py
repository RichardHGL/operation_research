import sys
import math
import copy
import numpy as np

def deal(ss, dic_relation):
	spcial_list = ['.', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	minus_flag = False
	number_flag = True
	var_flag = False
	star_flag = False
	temp_str = ""
	temp_str_1 = ""
	temp_num = 0.00
	length = len(ss)
	i = 0
	while(i < length):
		if number_flag and ss[i] not in spcial_list:
			if temp_str == "":
				if minus_flag:
					temp_num = -1
				else:
					temp_num = 1
			else:
				temp_num = eval(temp_str)
			minus_flag = False
			number_flag = False
			var_flag = True
			temp_str = ""
		if var_flag:
			while i < length and ss[i] != '+' and ss[i] != '-':
				if ss[i] == '*':
					temp_str_1 = copy.deepcopy(temp_str)
					temp_str = ""
					star_flag = True
					i += 1
				temp_str += ss[i]
				i += 1
			if star_flag:
				try:
					if temp_str == temp_str_1:
						dic_relation[temp_str_1][temp_str] = 2 * temp_num
					else:
						dic_relation[temp_str_1][temp_str] = temp_num
						dic_relation[temp_str][temp_str_1] = temp_num
				except:
					print "Key error:"
					print temp_str_1
					print temp_str
					sys.exit(0)
				star_flag = False
			else :
				dic_relation[temp_str]['1'] = temp_num
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
			return eval(temp_str)
			#dic_relation['1'] = eval(temp_str)
		elif var_flag:
			print "Error expresssion in End of !" +ss
			#vars.add(temp_str)
			#dic_relation.setdefault(temp_str, {})
	return 0
	

def newtown(filename, output, limit):
	f = open(filename)
	Myvec = []
	vec_vars = []
	idx = 0
	dic_relation = {}
	final_num = 0
	for line in f:
		if idx == 0:
			line = line.strip().split(" ")
			for item in line:
				vec_vars.append(item.split("=")[0])
				Myvec.append(eval(item.split("=")[1]))
			for item in vec_vars:
				dic_relation.setdefault(item, {})
				for item2 in vec_vars:
					dic_relation[item][item2] = 0.00
				dic_relation[item]['1'] = 0.00
		if idx == 1:
			line = line.strip().replace(" ", "").split("=")
			final_num = deal(line[1], dic_relation)
			break
		idx += 1
	f.close()
	print dic_relation
	mat_list = []
	temp_vec = []
	for item in vec_vars:
		temp_vec = []
		for item2 in vec_vars:
			temp_vec.append(dic_relation[item][item2])
		mat_list.append(temp_vec)
	#Mymat = np.mat(zeros(len(vec_vars), len(vec_vars)))
	temp_vec = []
	for item in vec_vars:
		temp_vec.append(dic_relation[item]['1'])
	A = np.mat(mat_list)
	temp = np.linalg.eigvals(A)
	if(np.all(temp) > 0 ):
		print "A is positive-definite!"
	else:
		print "A isn't positive-definite!"
		sys.exit(0)
	B = np.mat(temp_vec)
	X = np.mat(Myvec)
	while(True):
		delta = A.I * (A * X.T + B.T)
		result = X - delta.T
		temp = A.I * (A * result.T + B.T)
		num_de = temp.T * temp
		if float(num_de) < limit:
			print num_de
			break
		else:
			X = result
		
	f = open(output, "w")
	for i in range(0, len(vec_vars)):
		f.write(vec_vars[i] + "=" + str(result[0, i]) + "\n")
	f.close()
	'''
	
	for item in dic_relation:
		f.write(item)
		for item2 in dic_relation[item]:
			f.write(" " + item2 + ":" + str(dic_relation[item][item2]))
		f.write("\n")
	f.write("final = " + str(final_num))
	f.close()
	'''
	
	
if __name__ == '__main__':
	print "usage python newtown.py filename output limit"
	newtown(sys.argv[1], sys.argv[2], eval(sys.argv[3]))