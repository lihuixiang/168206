book = dict()  （查找）映射关系
book["apple"] = 9
book["avocado"] = 3
book["milk"] = 6

    投票(防止重复）
voted = {}
def  check_voter(name):  //检查是否在散列表中
 if voted.get(name):   //名字重复
    print "kick  them  out!"
 else:
    voted[name] = True
    print "let  them  vote!"
    
    
      用作缓存
cache  = {}
def  get_page(url):
   if  cache.get(url):
       return  cache[url]
   else:
       data = get_data_from_server(url)
       cache[url] = data
       return  data
    
    
    
    
    
    
