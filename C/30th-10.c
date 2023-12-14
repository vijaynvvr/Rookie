#include <stdio.h>
int main()
{
    float a, b, ans;
    int op;
    do
    {
        printf("\nEnter two numbers: \n");
        scanf("%f %f", &a, &b);

        printf("---DISPLAYING MENU---\n");
        printf("Press:\n'1' for addition\n'2' for subtraction\n'3' for multiplication\n'4' for division\n'5' to  quit");
        printf("\nwhich operator to be used \n");
        scanf("%d", &op);
    switch(op)
    {
    case 1:
    ans=a+b;
    printf("the sum is %f \n", ans);
    break;
    case 2:
        ans=a-b;
    printf("the diff is %f \n", ans);
    break;
    case 3:
        ans=a*b;
    printf("the prod is %f \n", ans);
    break;
    case 4:
        ans=a/b;
       printf("the quotient is %f \n", ans);
    break;
    case 5:
    break;
    default:
    printf("wrong operator");
    }
    }
    while(op!=5);
    return 0;
}