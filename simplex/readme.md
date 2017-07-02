程序运行命令：
python Trans.py problem_file relax_problem Trans_problem
python simplex.py Trans_problem output
释义：
先将一般线性规划问题(每个变量都大于等于0,可为不等式)通过Trans.py 来加入松弛变量， 再检查是否需要添加人工变量
此处实现为大M法，即添加的人工变量会以10000为系数
simplex.py 是解有初识基的线性规划问题，每次会打印矩阵及检验数。
例子：
python Trans.py test2.txt mids trans_test2.txt
python simplex.py trans_test2.txt res_test2