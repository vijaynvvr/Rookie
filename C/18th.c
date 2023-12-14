#include <stdio.h>
int main()
{
    int unit;
    double amount;

    printf("Enter total units consumed:\n");
    scanf("%d", &unit);

    if (unit<=100) {
        amount = unit*1.5;
    }

    else if (unit<=300) {
        amount = 100*1.5 + (unit-100)*2;
    }

    else if (unit<=500) {
        amount = 100*1.5 + 200*2 + (unit-300)*2.5;
    }

    else {
        amount = 100*1.5 + 200*2 + 200*2.5 + (unit-500)*3.25;
    }

    printf("Electricity bill = Rs. %.2f", amount);

    return 0;
}