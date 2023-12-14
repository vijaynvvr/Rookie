#include <stdio.h>
int main()
{
    int n, reversedN = 0, remainder, originalN;
    printf("Enter an integer: ");
    scanf("%d", &n);
    originalN = n;

    while (n != 0)
    {
        remainder = n % 10;
        reversedN = reversedN * 10 + remainder;
        n /= 10;
    }

    if (originalN == reversedN)
    {
        printf("%d is a palindrome.", originalN);
    }
    else
    {
        printf("%d is not a palindrome", originalN);
    }
    return 0;
}

#include <stdio.h>
void main()
{
    int num, originalNum, rem, result = 0;
    printf("Enter a three digit integer: ");
    scanf("%d", &num);
    originalNum = num;

    while (originalNum != 0)
    {
        rem = originalNum % 10;
        result += rem * rem * rem;
        originalNum /= 10;
    }

    if (result == num)
    {
        printf("%d is an Armstrong number.", num);
    }
    else
    {
        printf("%d is not an Armstrong number.", num);
    }
}