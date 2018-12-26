//A说：不是我做的案
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
     if ((mur != 'A') + (mur == 'c') +(mur == 'D') + == 3)     //判断谁是罪犯
     {
         print("%c\n",mur);
      }
  }
      system("pause");
      return 0;
}


 运行结果：C假话
