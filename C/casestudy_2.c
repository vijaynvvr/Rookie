#include <stdio.h>

int main()
{
    int units_manufactured[3] = {3, 4, 5};
    int last_serial[3] = {24, 19, 9};
    printf("\nData available at the end of last month:\n");
    printf("\n|Model type\t|Units Manufactured\t|Last serial number\t|\n");
    printf("|Ups1\t\t|%d\t\t\t|%d\t\t\t|\n", units_manufactured[0], last_serial[0]);
    printf("|Ups2\t\t|%d\t\t\t|%d\t\t\t|\n", units_manufactured[1], last_serial[1]);
    printf("|Ups3\t\t|%d\t\t\t|%d\t\t\t|\n", units_manufactured[2], last_serial[2]);
    int new_serial[3];
    for (int i = 0; i < 3; i++)
        new_serial[i] = last_serial[i] + units_manufactured[i];
    printf("\nData available at the end of new month:\n");
    printf("\n|Model type\t|Units Manufactured\t|New serial number\t|\n");
    printf("|Ups1\t\t|%d\t\t\t|%d\t\t\t|\n", units_manufactured[0], new_serial[0]);
    printf("|Ups2\t\t|%d\t\t\t|%d\t\t\t|\n", units_manufactured[1], new_serial[1]);
    printf("|Ups3\t\t|%d\t\t\t|%d\t\t\t|\n", units_manufactured[2], new_serial[2]);
    return 0;
}