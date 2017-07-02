此压缩包内包含以下程序：
utils.py:记录常用操作
random_graph.py:生成联通的无向图(也可将生成边部分稍作修改变为生成有向图)
Dijkstra.py:Dijkstra算法实现
Max_flow.py: 最大流算法实现
Bellan_ford.py: Bellan_ford算法实现,用于计算带负边的单源最短路径(距离)
max_flow_min_cost.py:最小费用的最大流，其中用到Max_flow.py来计算最大流,用到Bellman_ford算法来求从源节点到目标节点的最短路径
输入格式：
Dijkstra输入格式为\t分隔的三元组,即src	aim	weight来代表图中的边
Max_flow输入格式为\t分隔的三元组,即src	aim	capacity来代表图中的边
max_flow_min_cost输入格式为\t分隔的四元组,即src	aim	capacity cost来代表图中的边
max_flow和max_flow_min_cost主要处理部分均可用如下伪代码表示:
	while true:
		if exist_augment_path:
			path = find_augment_path
			update(path)
		else:
			break
			
运行命令:
此大作业第一部分运行如下：
python random_graph.py size output_graph
python Dijkstra.py output_graph res_output_graph
第二部分最大流运行如下：
python Max_flow.py graph_file res_output
python max_flow_min_cost.py graph_file res_output

运行实例:
python random_graph.py 30 C_graph.txt
python Dijkstra.py C_graph.txt res_MST.txt
此处的res_MST.txt仅包含最小生成树，获得最短路径的部分为Dijkstra的find_way函数会在运行时打出结果，但不存到文件
python Max_flow.py test_book.txt res_book
python max_flow_min_cost.py test_book_2.txt res_book_2
其结果文件均为当前的各边流的情况,至于最大流的量和最小费用则会在屏幕打出。这两个运行程序均是使用书中的例子
我将其分别命名为test_book.txt和test_book_2.txt
