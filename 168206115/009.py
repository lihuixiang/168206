#user/python3
for  num  in  range(100,1000) #依次取出num的值，第一次101，最后一次999
bai = num //100
shi = num //10 % 10
ge = num % 10
if(bai**3+shi**3+ge**3 ==num):
print (num, end = ' ')  #使输出的数不换行，以空格隔开同行输出
