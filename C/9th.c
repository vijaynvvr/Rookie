#include<stdio.h>

int main()
{
    int a=9,b=7,c;
    c = a&b;
    printf("Line 1 - Value of c is %d\n",c);
    c = a|b;
    printf("Line 2 - Value of c is %d\n",c);
    c = a^b;
    printf("Line 3 - Value of c is %d\n",c);
    c = ~a;
    printf("Line 4 - Value of c is %d\n",c);
    c = a << 2;
    printf("Line 5 - Value of c is %d\n",c);
    c = a >> 2;
    printf("Line 6 - Value of c is %d\n",c);
    return 0;
}
