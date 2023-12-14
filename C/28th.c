#include "stdio.h" 
int main()
{
 int tv17box,tv22box,tv26box,tv32box,tv37box;
 int tv17num=98,tv22num=79,tv26num=65,tv32num=43,tv37num=17;
 tv17box = 1;
 tv22box = 2;
 tv26box = 3;
 tv32box = 4;
 tv37box = 5;
 printf("\nEnter number of TV-LCD 17 model to be packed:%d",tv17num);                  
 printf("\nEnter number of TV-LCD 22 model to be packed:%d",tv22num);
 printf("\nEnter number of TV-LCD 26 model to be packed:%d",tv26num);
 printf("\nEnter number of TV-LCD 32 model to be packed:%d",tv32num);
  printf("\nEnter number of TV-LCD 37 model to be packed:%d\n",tv37num);
 printf("\n      ** Requisition Note **  ");
 printf("\n ========================================");
 
 printf("\n     TV Model   |  Box type  |  Numbers ");
 printf("\n                |  required  |   ");
 
 printf("\n ========================================");
 
 printf("\n     TV-LCD 17         %d           %d",tv17box,tv17num);
 printf("\n     TV-LCD 22         %d           %d",tv22box,tv22num);
 printf("\n     TV-LCD 26         %d           %d",tv26box,tv26num);
 printf("\n     TV-LCD 32         %d           %d",tv32box,tv32num);
 printf("\n     TV-LCD 37         %d           %d",tv37box,tv37num);
 printf("\n ========================================");
 
 return 0;
 
 }