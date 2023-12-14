#include <stdio.h>

int main()
{
    int a,b,c,d,e,f,g;
    printf("Enter three values:");
    scanf("%d %d %d", &a, &b, &c);
    d = -a+b*c;
    e = (a+b)*c;
    f = (a*b)/c;
    g = a*(b/c);
    printf("\na=%d b=%d c=%d\n",a,b,c);
    printf("-%d+%d*%d = %d\n", a, b, c, d);
    printf("(%d+%d)*%d = %d\n", a, b, c, e);
    printf("(%d*%d)/%d = %d\n", a, b, c, f);
    printf("%d*(%d/%d) = %d\n", a, b, c, g);

    return 0;
}