// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>

// int main()
// {
//     srand(time(0));
//     int marbles;
//     int low = 10, high = 100;
//     marbles = rand() % (high - low + 1) + low;
//     marbles = 5;
//     printf("\nThe initial size of the pile of marbles is: %d \n", marbles);
//     int you, stupidComp, smartComp, comp;
//     int marbles_left = marbles;
//     int toss = rand() % 2;
//     if (toss)
//         printf("\nYou won the toss, first chance to choose the marbles is yours!\n");
//     else
//         printf("\nYou lost the toss, computer is going to choose the marbles first.!\n");
//     int compIntelligence = rand() % 2;
//     compIntelligence = 0;
//     int flag;
//     if (compIntelligence)
//     {
//         printf("\nThe computer is going to play smartly!\n");
//     }
//     else
//     {
//         printf("\nThe computer is going to play stupidly.\n");
//         do
//         {
//             switch (toss)
//             {
//             case 0:
//                 comp = rand() % (marbles_left / 2) + 1;
//                 marbles_left -= comp;
//                 printf("\nComputer chose %d marbles\n", comp);
//                 printf("\n%d marbles left, now your turn.\n", marbles_left);
//                 flag = 0;
//                 scanf("%d", &you);
//                 marbles_left -= you;
//                 printf("\nYou chose %d marbles\n", you);
//                 printf("\n%d marbles left.\n", marbles_left);
//                 flag = 1;
//                 break;
//             case 1:
//                 printf("\n%d marbles left, your turn.\n", marbles_left);
//                 scanf("%d", &you);
//                 printf("\nYou chose %d marbles\n", you);
//                 marbles_left -= you;
//                 printf("\n%d marbles left.\n", marbles_left);
//                 flag = 1;
//                 comp = rand() % (marbles_left / 2) + 1;
//                 printf("\nComputer chose %d marbles\n", comp);
//                 marbles_left -= comp;
//                 flag = 0;
//                 break;
//             }
//         } while (marbles_left != 1);
//     }
//     if (flag)
//         printf("\nYou won the game!");
//     else
//         printf("\nYou lost the game.\n");

//     return 0;
// }

// #include <stdio.h>

// int main()
// {
//     int units_manufactured[3];
//     for (int i = 0; i < 3; i++)
//     {
//         printf("Enter the units manufactured for ups%d:\n", i+1);
//         scanf("%d", &units_manufactured[i]);
//     }
//     int last_serial[3] = {24, 19, 9};
//     printf("\nData available at the end of last month:\n");
//     printf("\n|Model type\t|Units Manufactured\t|Last serial number\t|\n");
//     printf("|Ups1\t\t|%d\t\t\t|%d\t\t\t|\n", units_manufactured[0], last_serial[0]);
//     printf("|Ups2\t\t|%d\t\t\t|%d\t\t\t|\n", units_manufactured[1], last_serial[1]);
//     printf("|Ups3\t\t|%d\t\t\t|%d\t\t\t|\n", units_manufactured[2], last_serial[2]);
//     int new_serial[3];
//     for (int i = 0; i < 3; i++)
//         new_serial[i] = last_serial[i] + units_manufactured[i];
//     printf("\nData available at the end of new month:\n");
//     printf("\n|Model type\t|Units Manufactured\t|New serial number\t|\n");
//     printf("|Ups1\t\t|%d\t\t\t|%d\t\t\t|\n", units_manufactured[0], new_serial[0]);
//     printf("|Ups2\t\t|%d\t\t\t|%d\t\t\t|\n", units_manufactured[1], new_serial[1]);
//     printf("|Ups3\t\t|%d\t\t\t|%d\t\t\t|\n", units_manufactured[2], new_serial[2]);
//     return 0;
// }

// #include <stdio.h>
// struct studInfo
// {
//     int marks;
//     int admnNo;
//     char name[20];
// } stud[3];
// int main()
// {
//     for (int i = 0; i < 3; i++)
//     {
//         printf("Enter name of student-%d: ", i+1);
//         scanf("%s", stud[i].name);
//         printf("Enter admission number of student-%d: ", i+1);
//         scanf("%d", &stud[i].admnNo);
//         printf("Enter marks of student-%d: ", i+1);
//         scanf("%d", &stud[i].marks);
//     }
//     printf("\nStudent details:\n");
//     for (int i = 0; i < 3; i++)
//     {
//         printf("\nName of student-%d: %s", i+1, stud[i].name);
//         printf("\nAdmission no. of student-%d: %d\n", i+1, stud[i].admnNo);
//         printf("\nMarks of student-%d: %d", i+1, stud[i].marks);
//     }
//     return 0;
// }

// #include<stdio.h>
// int main()
// {
//     char a[30][20],i,b[30][20];
//     int n;
//     printf("Enter the number of words of encrypted message\n");
//     scanf("%d",&n);
//     printf("Enter the message\n");
//     for(i=0;i<n;i++)
//         scanf("%s",a[i]);
//     for(i=0;i<n;i++)
//         strcpy(b[i],strrev(a[i]));
//     printf("The encrypted message is\n");
//     for(i=0;i<n;i++)
//         printf("%s ",b[i]);
//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>

// int main()
// {
//     int *ptr;
//     ptr = (int*)malloc(10*sizeof(int));
//     for (int i = 0; i < 10; i++)
//     {
//         ptr[i] = 7*(i+1);
//         printf("7 X %d = %d \n", i+1, ptr[i]);
//     }
//     printf("\nAfter Reallocation\n");
//     ptr = (int*)realloc(ptr, 15*sizeof(int));
//     for (int i = 0; i < 15; i++)
//     {
//         ptr[i] = 7*(i+1);
//         printf("7 X %d = %d \n", i+1, ptr[i]);
//     }
//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>

// int main()
// {
//     int *ptr;

//     ptr = (int *)malloc(2 * sizeof(int));
//     //printf("%u", ptr);

//     for (int i = 0; i < 2; i++)
//     {
//         scanf("\n%d", &ptr[i]);
//     }
//     for (int i = 0; i < 2; i++)
//     {
//         printf("\n%d", ptr[i]);
//     }
//     printf("\n");
//     free(ptr);
//     for (int i = 0; i < 2; i++)
//     {
//         printf("\n%d", ptr[i]);
//     }
//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>
// #include <conio.h>
// #include <time.h>

// int main()
// {
//     srand(time(0));
//     int you, comp;
//     printf("Enter your value between 1 to 999: ");
//     scanf("%d", &you);
//     comp = rand()%999 + 1;
//     printf("you = %d\n", you);
//     printf("comp = %d\n", comp);
//     int attempt = 1;
//     while(1)
//     {
//         if (you == comp)
//         {
//             printf("Yours and comp values matched at attempt no. %d\n", attempt);
//             break;
//         }
//         if (kbhit())
//             break;
//         attempt++;
//         comp = rand()%100 + 1;
//     }
//     return 0;
// }

#include <stdio.h>
#include <conio.h>

int main()
{
    int a;
    printf("Enter the value of a: ");
    scanf("%d", &a);
    int b = 1;
    while(1)
    {
         if (kbhit())
             break;
        printf("%d\n", b);
        if (a==b)
        {
            printf("Matched");
            break;
        }
        b++;
    }
    return 0;
}