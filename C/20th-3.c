#include<stdio.h>
int main()
{
    long int factorial = 1;
    int i, n;
    printf("Enter a positive number to find it's factorial:\n");
    scanf("%d", &n);

    for(i=1; i<=n; i++) {
        factorial = factorial*i; 
    }

    printf("%ld", factorial);

}