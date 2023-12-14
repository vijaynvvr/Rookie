#include<stdio.h>
int main() {
    int n;
    printf("Enter number of terms:");
    scanf("%d", &n);
    float sum = 0;
    
    for (float i = 1; i <= n; i++) {
        sum = sum + 1/i ;
    }
    printf("%f", sum);
    return 0;
}