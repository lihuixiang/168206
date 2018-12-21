node = find_lowest_cost_node(costs)//找最小节点
while  node  is  not  None:  //这个循环在所有结点处理过后结束
       cost = costs[node]
       neighbors = graph[node]
       for n  in  neighbors.keys(): ///遍历所有节点的邻居
           new_cost = cost + neighbors[n]
           if costs[n]>new_cost:  //如果该节点前往该邻居更近
               costs[n] = new_cost//就更新该邻居的开销
               parents[n] = node //将该邻居的父节点设置为当前节点
      processed.append(node) //将该节点标记处理过
      node = find_lowest_cost_node(costs)  //找出要处理的节点并循环
def find_lowest_cost_node(costs):
     lowest_cost = float("inf")
     lowest_cost_node = None
     for  node  in  costs://遍历所有节点
           cost = costs[node]
           if cost < lowest_cost  and  node  not in  processed:开销更低且未处理过
               lowest_cost  = cost//将其视为开销最低的节点
               lowest_cost_node = node
           return  lowest_cost_node
