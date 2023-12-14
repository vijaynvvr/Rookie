#include <stdio.h>

int main()
{
    int a,b,result;
    char op;

    printf("Enter the operator:");
    scanf(" %c", &op);

    printf("Enter values of two operands:");
    scanf("%d %d", &a, &b);
    
    switch (op)
    {
    case '/':
        result=a/b;
        printf("%d/%d=%d", a, b, result);
        break;
    case '*':
        result=a*b;
        printf("%d*%d=%d", a, b, result);
        break;
    case '%':
        result=a%b;
        printf("%d%%d=%d", a, b, result);
        break;
    case '+':
        result=a+b;
        printf("%d+%d=%d", a, b, result);
        break;
    case '-':
        result=a-b;
        printf("%d-%d=%d", a, b, result);
        break;
    default :
        printf("Invalid operator");                    
    }
    return 0;
}