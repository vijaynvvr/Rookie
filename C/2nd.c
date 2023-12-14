#include<stdio.h>

int main()
{
    int a;
    printf("Enter a value:");
    scanf("%d", &a);
    printf("\nDecimal value: " "%d\n", a);
    printf("Hexadecimal value: " "%x\n", a);
    printf("Octadecimal value: " "%o\n", a);
    return 0;
}