#include <stdio.h>

int main()
{
    int n;
    printf("Enter a value:");
    scanf("%d", &n);

    if (n>=0) {
        if (n>0) {
            printf("%d is positive", n);
        }
        else {
            printf("Entered value is 0");
        }
    }
    else {
        printf("%d is negative", n);
    }
    return 0;
}