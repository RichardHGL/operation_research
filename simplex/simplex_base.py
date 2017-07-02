import sys
import math
import re
import simplex_lib as lib
#def normalize():
	
def check_base(i ,vec):
	if vec[i] == 1.00:
		for j in range(0, len(vec)):
			if j != i and vec[j] != 0.00:
				return False
		return True
	return False
	
def find_base(var_name, num_line, var_para):
	indexes = []
	length = len(var_name)
	temp_vec2 = []
	for j in range(0, length):
		temp_vec = []
		for i in range(1, num_line):
			temp_vec.append(var_para[i][j])
		temp_vec2.append(temp_vec)
	for i in range(0, num_line - 1):
		if len(indexes) < i:
			print "Error no base for row " + str(i)
			sys.exit(0)
		for j in range(0, length):
			if var_name[j] == '1':
				continue
			if check_base(i, temp_vec2[j]):
				indexes.append(j)
				break
	return indexes

def get_check_num(var_name, base_list, var_para):
	check_num = []
	for k in range(0, len(var_name)):
		if var_name[k] == '1' or k in base_list:
			check_num.append(0.00)
			continue
		temp = 0.00
		for i in range(0, len(base_list)):
			temp += var_para[0][base_list[i]] * var_para[i + 1][k]
		check_num.append(var_para[0][k] - temp)
	return check_num
	
def judge(check_num):
	for i in range(0, len(check_num)):
		if check_num[i] > 0:
			return False
	return True
	
def get_max_place(check_num):
	max_place = 0
	max = check_num[0]
	for i in range(1, len(check_num)):
		if check_num[i] > max:
			max_place = i
			max = check_num[i]
	return max_place

def sort_by_value(d, k = 50): 
	items = d.items()
	backitems = [ [v[1], v[0] ] for v in items] 
	backitems.sort(comp)
	if len(backitems ) < k:
		return [ backitems[i][1] for i in range(0, len(backitems))], len(backitems)
	return [ backitems[i][1] for i in range(0, k)], k	
	
def change_base(base_list, b, var_para, max_place, num_colomn):
	temp_min = -1.00
	min = -1.00
	in_base = max_place
	out_base = 0
	for i in range(1, len(var_para) ):
		if var_para[i][max_place] > 0:
			#print type(b[i]), type(var_para[i][max_place])
			temp_min = b[i - 1] / var_para[i][max_place]
			out_base = i
			break
	if temp_min == -1:
		print "No out_base"
		sys.exit(0)
	for i in range(1, len(var_para) ):
		if var_para[i][max_place] > 0:
			temp = b[i - 1] / var_para[i][max_place]
			if temp < temp_min:
				temp_min = temp
				out_base = i
	base_list[out_base - 1] = in_base# change the base
	# normalize the out_base row
	temp_num = var_para[out_base][in_base]
	b[out_base - 1] /= temp_num
	for j in range(0, num_colomn):
		var_para[out_base][j] /= temp_num
	#normalize other rows
	for i in range(1, len(var_para)):
		if i == out_base or var_para[i][in_base] == 0.00:
			continue
		times = var_para[i][in_base]#var_para[out_base][in_base] = 0.00
		b[i - 1] -= b[out_base - 1] * times
		for j in range(0, num_colomn):
			var_para[i][j] -= var_para[out_base][j] * times
	print "Chage Base done."
	
def deal(filename, output):
	var_name = lib.pre_deal(filename)
	num_line, var_para, b =  lib.mid_deal(var_name, filename)
	base_list = find_base(var_name, num_line, var_para)
	check_num = get_check_num(var_name, base_list, var_para)
	f1 = open(output, "w")
	f1.write("\t".join(var_name) + "\n")
	steps = 0
	while( not judge(check_num) ):
		steps += 1
		max_place = get_max_place(check_num)
		f1.write("steps " + str(steps) + "\n")
		f1.write("check_num = \n")
		f1.write("\t".join([str(item) for item in check_num]) + "\n")
		#print "steps " + str(steps)
		if steps % 10 == 0:
			print "Continue? If so, print Y, Else exit"
			t_str = raw_input("Continue? If so, print Y, Else exit")
			if t_str != 'Y':
				break
		print max_place, len(var_name)
		change_base(base_list, b, var_para, max_place, len(var_name))
		check_num = get_check_num(var_name, base_list, var_para)
	for i in range(0, len(var_name)):
		if var_name[i] == "1":
			continue
		f1.write(var_name[i] + "\t")
	f1.write("\n")
	for i in range(0, len(var_name)):
		if var_name[i] == "1":
			continue
		if i in base_list:
			f1.write(str(b[base_list.index(i)]) + "\t")
		else :
			f1.write(str(0) + "\t")
	f1.close()
	
if __name__ == '__main__':
	print "usage: python simplex.py problem_file output"
	deal(sys.argv[1], sys.argv[2])