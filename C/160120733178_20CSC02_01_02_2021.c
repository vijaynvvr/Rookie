//(1)

// (A) To find the factorial of a given number:-
// #include <stdio.h>

// int main()
// {
//     long int fact = 1;
//     int n;
//     printf("\nEnter value of n:\n");
//     scanf("%d", &n);
//     for (int i = 1; i <= n; i++) 
//     {
//         fact = fact * i;
//     }
//     printf("Factorial is %d", fact);
//     return 0;
// }

// (B) To print following triangle of numbers by using nested loops:-
//   1
//  1 2
// 1 2 3
// #include <stdio.h>

// int main()
// {
//     for (int line = 1; line <= 3; line++)
//     {
//         for (int gap = 1; gap <= (3-line); gap++) 
//         {
//             printf(" ");
//         }
//         for (int num = 1; num <= line; num++) 
//         {
//             printf("%2d", num);
//         }
//         printf("\n");
//     }
//     return 0;
// }