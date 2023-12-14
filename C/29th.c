#include <stdio.h>

void largest (int a, int b, int c);

void largest (int a, int b, int c) {
    int max;
    max = a > b ? a > c ? a : c : b > c ? b : c;
    printf("Largest of three numbers is %d\n", max);
}
int main(void)
{
    int a,b,c;
    int x,y,z;

    printf("Enter three numbers:\n");
    scanf("%d %d %d", &a, &b, &c);
    largest(a,b,c);
    
    printf("\nEnter three numbers:\n");
    scanf("%d %d %d", &x, &y, &z);
    largest(x,y,z);

    return 0;
}