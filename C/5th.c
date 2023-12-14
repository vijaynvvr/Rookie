#include <stdio.h>
int main()
{
    int a,b,c,d;
    printf("Enter three values:");
    scanf("%d %d %d", &a, &b, &c);
    d = a > b ? a > c ? a : c : b > c ? b : c ;
    printf("a=%d b=%d c=%d\n", a, b, c);
    printf("Max of three numbers is %d", d);

    return 0;
}