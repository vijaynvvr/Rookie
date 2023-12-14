#include <stdio.h>

int main()
{
    int n,num,sum=0,rem=0;
    printf("Enter an integer:");
    scanf("%d", &n);
    num=n;
    while(n!=0) {
        rem = n%10;
        sum=sum+rem;
        n=n/10;
    }
    printf("The sum of digits of %d is %d", num, sum);
    return 0;
}

#include <stdio.h>

int main()
{
    int n, num, rem, rev=0;
    printf("Enter an integer:");
    scanf("%d", &n);
    num = n;
    while (n!=0) {
        rem = n%10;
        rev = rev*10+rem;
        n = n/10;
    }
    printf("Reverse of %d is %d", num, rev);
    return 0;
}

