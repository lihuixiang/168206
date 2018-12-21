def  search(name):
search_queue = deque()//创建队列
search_queue +=graph["name"]//将名字加入到这个队列
searched = []//记录检查过的人
while search_queue:
     person = search_queue.popleft()
     if  person  not  in  searched://仅当这个人没检查过才检查
       if  person_is_seller(person):
           print  person + " is  a  mango  seller!"
           return  True
      else:
          search_queue += graph[person]
          search.append(person)//将这个人标记为检查过
          return  False
          
          
          
