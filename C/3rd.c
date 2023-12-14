#include<stdio.h>

int main()
{
    int n;
    printf("Enter a number:");
    scanf("%d", &n);
    printf("%d \n", n);
    printf("%04d \n", n);
    printf("%06d \n", n);
    printf("%6d \n", n);
    printf("%-6d \n", n);
    return 0;
}