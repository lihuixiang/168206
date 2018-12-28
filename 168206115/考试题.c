 1.//A说：不是我做的案
  //B说：D是罪犯
  //C说：B是盗窃这块钻石的罪犯
  //D说：B有意诬陷我
  //已知三人说真话，一人假话

#include <stdio.h>
#include <stdlib.h>
int  main()
{
  char  mur = 0;
  for (mur = 'A'; mur <= 'D'; mur++)
  {
     if ((mur != 'A') + (mur == 'D') + (mur == 'B') +（mur ！== 'D')  == 3)     //判断谁是罪犯  三真一假
     {
         print("%c\n",mur);
      }
  }
      system("pause");
      return 0;
}


 运行结果：B
 
 
 
 
 2.//A说：不是我做的案
  //B说：D是罪犯
  //C说：B是盗窃这块钻石的罪犯
  //D说：B有意诬陷我
  //已知三人说假话，一人说真话
  
   #include <stdio.h>
   #include <string.h>
   int  main()
 {
   char arr[] = {'A','B','C','D'}
   int i = 0;
   for (i = 0;i < 4;i++)   //遍历
   { 
     if ((arr[i]!='A') + (arr[i]='D') + (arr[i]='B') + (arr[i]!='D') = 1))   //一真三假
        {print("罪犯是%c\n",arr[i]; //找到罪犯}
   }
               system("pause");
               return 0;
 }
     运行结果：罪犯是A


   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
