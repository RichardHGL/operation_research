��ѹ�����ڰ������³���
utils.py:��¼���ò���
random_graph.py:������ͨ������ͼ(Ҳ�ɽ����ɱ߲��������޸ı�Ϊ��������ͼ)
Dijkstra.py:Dijkstra�㷨ʵ��
Max_flow.py: ������㷨ʵ��
Bellan_ford.py: Bellan_ford�㷨ʵ��,���ڼ�������ߵĵ�Դ���·��(����)
max_flow_min_cost.py:��С���õ�������������õ�Max_flow.py�����������,�õ�Bellman_ford�㷨�����Դ�ڵ㵽Ŀ��ڵ�����·��
�����ʽ��
Dijkstra�����ʽΪ\t�ָ�����Ԫ��,��src	aim	weight������ͼ�еı�
Max_flow�����ʽΪ\t�ָ�����Ԫ��,��src	aim	capacity������ͼ�еı�
max_flow_min_cost�����ʽΪ\t�ָ�����Ԫ��,��src	aim	capacity cost������ͼ�еı�
max_flow��max_flow_min_cost��Ҫ�����־���������α�����ʾ:
	while true:
		if exist_augment_path:
			path = find_augment_path
			update(path)
		else:
			break
��������:
�˴���ҵ��һ�����������£�
python random_graph.py size output_graph
python Dijkstra.py output_graph res_output_graph
�ڶ�����������������£�
python Max_flow.py graph_file res_output
python max_flow_min_cost.py graph_file res_output

����ʵ��:
python random_graph.py 30 C_graph.txt
python Dijkstra.py C_graph.txt res_MST.txt
�˴���res_MST.txt��������С��������������·���Ĳ���ΪDijkstra��find_way������������ʱ�������������浽�ļ�
python Max_flow.py test_book.txt res_book
python max_flow_min_cost.py test_book_2.txt res_book_2
�����ļ���Ϊ��ǰ�ĸ����������,�����������������С�����������Ļ��������������г������ʹ�����е�����
�ҽ���ֱ�����Ϊtest_book.txt��test_book_2.txt