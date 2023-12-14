#include <stdio.h>

int main()
{
    int a,b,c;
    printf("Enter three values:\n");
    scanf("%d %d %d", &a, &b, &c);

    if (a>b && a>c) {
        printf("Max is %d", a );
    }
    if (b>a && b>c) {
        printf("Max is %d", b );
    }
    if (c>a && c>b) {
        printf("Max is %d", c );
    }
    return 0;
}