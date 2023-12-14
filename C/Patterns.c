//Pattern-1
//for row = 4,
// |*
// |**
// |***
// |****

// #include <stdio.h>

// int main()
// {
//     int row;
//     printf("Enter the number rows:\n");
//     scanf("%d", &row);

//     for (int i = 1; i <= row; i++)
//     {
//         for (int j = 1; j <= i; j++)
//         {
//             printf("*");
//         }
//         printf("\n");
//     }
//     return 0;
// }

//Pattern-2
//for n=4,
// |1
// |1  2
// |1  2  3
// |1  2  3  4

// #include <stdio.h>

// int main()
// {
//     int r;
//     printf("Enter the number of rows:\n");
//     scanf("%d", &r);
//     for (int i=1; i<=r; i++)
//     {
//         for (int j=1; j<=i; j++)
//         {
//             printf("%3d ", j);
//         }
//         printf("\n");
//     }
//     return 0;
// }

//Pattern-3
//for n=3
// |1
// |1  2
// |1  2  3
// |1  2
// |1

// #include <stdio.h>

// int main()
// {
//     int n;
//     printf("Enter the value of n:\n");
//     scanf("%d", &n);
//     for (int i = 1; i <= n; i++)
//     {
//         for (int j = 1; j <= i; j++)
//         {
//             printf("%3d", j);
//         }
//         printf("\n");
//     }
//     for (int i = 1; i < n; i++)
//     {
//         for (int j = 1; j <= (n - i); j++)
//         {
//             printf("%3d", j);
//         }
//         printf("\n");
//     }

//     return 0;
// }

//Pattern-4
//for n=3
// |  1
// | 1 2
// |1 2 3

// #include <stdio.h>

// int main()
// {
//     int row;
//     printf("Enter the number of rows:\n");
//     scanf("%d", &row);
//     for (int i = 1; i <= row; i++)
//     {
//         for (int gap = 1; gap <= (row-i); gap++)
//         {
//             printf(" ");
//         }
//         for (int num = 1; num <= i; num++)
//         {
//             printf("%2d", num);
//         }
//         printf("\n");
//     }
//     return 0;
// }

//Pattern-5
//for n=4,
// |   ****
// |  ****
// | ****
// |****

// #include <stdio.h>

// int main()
// {
//     int row;
//     printf("Enter number of rows:\n");
//     scanf("%d", &row);
//     for (int i = 1; i <= row; i++)
//     {
//         for (int gap = 1; gap <= (row-i); gap++)
//         {
//             printf(" ");
//         }
//         for (int star = 1; star <= row; star++)
//         {
//             printf("*");
//         }
//         printf("\n");
//     }
//     return 0;
// }

//Pattern-6
//for row=5,
// |1
// |1   4
// |1   4   9
// |1   4   9   16
// |1   4   9   16   25

// #include <stdio.h>

// int main()
// {
//     int row;
//     printf("Enter number of rows:\n");
//     scanf("%d", &row);
//     for (int i = 1; i <= row; i++)
//     {
//         for (int j = 1; j <= i; j++)
//         {
//             printf("%4d", j*j);
//         }
//         printf("\n");
//     }
//     return 0;
// }

//Pattern-7
//for row=5,
// |1   6  10  13  15
// |2   7  11  14
// |3   8  12
// |4   9
// |5

// #include <stdio.h>

// int main()
// {
//     int row;
//     printf("Enter the number of rows:\n");
//     scanf("%d", &row);
//     int num = 1;
//     for (int i = 1; i <= row; i++)
//     {
//         int k = 0;
//         for (int j = 1; j <= (row - i + 1); j++)
//         {
//             printf("%3d ", num);
//             num = num + (row - k);
//             k++;
//         }
//         printf("\n");
//         for (num = 1; num <= i; num++);
//     }
//     return 0;
// }

//Password-Generator

// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>

// int main()
// {
//     srand(time(0));
//     int n;
//     printf("How many digits password you need?\n");
//     scanf("%d", &n);
//     for (int i = 1; i <= n; i++)
//     {
//         int num = rand()%10;
//         printf("%d", num);
//     }
//     return 0;
// }