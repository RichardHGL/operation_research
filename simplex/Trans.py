import sys
import math
import re
import simplex_lib as lib
#def normalize():

def relax_Trans(filename1, filename2):
	f = open(filename1)
	f1 = open(filename2, "w")
	idx = 0
	temp_vars = []
	temp_paras = []
	relax_num = 0
	b = []
	for line in f:
		temp4 = 0
		line = line.strip().replace(" ", "")
		if line == "":
			continue
		idx += 1
		if idx == 1:
			f1.write(line + "\n")
		else :
			temp1 = line.find(">");
			temp2 = line.find("<")
			if temp1 > 0:
				#f1.write(line[:temp1])
				temp_vars,temp_paras = lib.get_paras( line[:temp1] )
				temp_vars.append("relax_" + str(relax_num))
				relax_num += 1
				temp_paras.append(-1.00)
			elif temp2 > 0:
				#f1.write(line[:temp2])
				temp_vars,temp_paras = lib.get_paras( line[:temp2] )
				temp_vars.append("relax_" + str(relax_num))
				relax_num += 1
				temp_paras.append(1.00)
			if '1' in temp_vars:
				temp3 = temp_vars.index('1')
				temp4 = temp_paras[temp3]
			if temp_vars[0] != '1':
				if temp_paras[0] == 1:
					f1.write(temp_vars[0])
				elif temp_paras[0] == -1:
					f1.write("-" + temp_vars[0])
				else:
					f1.write(str(temp_paras[0]) + temp_vars[0])
			for i in range(1, len(temp_vars)):
				if temp_vars[i] != '1':
					if temp_paras[i] > 0:
						if temp_paras[i] == 1:
							f1.write("+" + temp_vars[i])
						else:
							f1.write("+" + str(temp_paras[i]) + temp_vars[i])
					elif temp_paras[i] < 0:
						if temp_paras[i] == -1:
							f1.write("-" + temp_vars[i])
						else:
							f1.write(str(temp_paras[i]) + temp_vars[i])
						#f1.write(str(temp_paras[i]) + temp_vars[i])
			f1.write("=" + str(eval(line.split("=")[1]) - temp4) + "\n")
	f1.close()
	f.close()
	
def art_Trans(filename1, filename2):
	var_name = lib.pre_deal(filename1)
	num_line, var_para, b =  lib.mid_deal(var_name, filename1)
	length = len(var_name)
	temp_vec2 = []
	f = open(filename1)
	f1 = open(filename2, "w")
	art_vars = {}
	art_num = 0
	for j in range(0, length):
		temp_vec = []
		for i in range(1, num_line):
			temp_vec.append(var_para[i][j])
		temp_vec2.append(temp_vec)
	for i in range(0, num_line - 1):
		for j in range(0, length):
			if var_name[j] == '1':
				continue
			if check_base(i, temp_vec2[j]):
				break
			else :
				if j == length - 1:
					art_vars[i] = "art_" + str(art_num)
					art_num += 1
	idx = 0
	for line in f:
		line = line.strip()
		if idx == 0:
			f1.write(line + "\n")
		else:
			if idx in art_vars:
				line = line.split("=")
				f1.write(line[0] + "+10000" +art_vars[idx] + "=" + line[1] + "\n")
			else:
				f1.write(line + "\n")
		idx += 1
	f1.close()
	f.close()
	
def check_base(i ,vec):
	if vec[i] == 1.00:
		for j in range(0, len(vec)):
			if j != i and vec[j] != 0.00:
				return False
		return True
	return False
	
if __name__ == '__main__':
	print "usage: python Trans.py problem_file mids output"
	relax_Trans(sys.argv[1], sys.argv[2])
	art_Trans(sys.argv[2], sys.argv[3])