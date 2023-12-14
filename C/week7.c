// (1) Program to illustrate initialization of arrays of one dimension:-
// #include <stdio.h>

// int main()
// {
//     int n;
//     printf("Enter the size of the array:\n");
//     scanf("%d", &n);
//     int marks[n];

//     for (int i = 0; i < n; i++)
//     {
//         printf("Enter marks of sub-%d: ", i+1);
//         scanf("%d", &marks[i]);
//     }

//     for(int i = 0; i < n; i++)
//     {
//         printf("Marks of sub-%d are %d.\n", i+1, marks[i]);
//     }
//     return 0;
// }

// (2) Program to find the sum and average of the values in a 1-D array:-
// #include <stdio.h>

// int main()
// {
//     int n;
//     printf("Enter the size of the array:\n");
//     scanf("%d", &n);
//     int x[n];

//     printf("Enter the elements of the array:\n");
//     for (int i = 0; i < n; i++)
//     {
//         scanf("%d", &x[i]);
//     }

//     float sum = 0;
//     for (int i = 0; i < n; i++)
//     {
//         sum = sum + x[i];
//     }
//     printf("Sum of elements of array is %0.2f.\n", sum);

//     printf("Average of elements of array is %0.2f.\n", sum/n);
//     return 0;
// }

// (3) Program to find the minimum and the maximum in a list of values:-
// #include <stdio.h>

// int main()
// {
//     int n;
//     printf("Enter the size of the array:\n");
//     scanf("%d", &n);
//     int x[n];

//     printf("Enter the elements of the array:\n");
//     for (int i = 0; i < n; i++)
//     {
//         scanf("%d", &x[i]);
//     }

//     int min = x[0];
//     int max = x[0];
//     for (int i = 0; i < n; i++)
//     {
//         if (min>x[i])
//         {
//             min=x[i];
//         }
//     }
//     for (int i = 0; i < n; i++)
//     {
//         if (max<x[i])
//         {
//             max=x[i];
//         }
//     }
//     printf("\nMax and Min in the list of elements in array are %d and %d.", max, min);
//     return 0;
// }

// (4) Program to print the array elements in reverse order:-
// #include <stdio.h>

// int main()
// {
//     int n;
//     printf("Enter the size of the array:\n");
//     scanf("%d", &n);
//     int x[n];

//     printf("Enter the elements  of the array:\n");
//     for (int i = 0; i < n; i++)
//     {
//         scanf("%d", &x[i]);
//     }

//     printf("Elements of the array in reverse order are:\n");
//     for (int i = n-1; i >= 0; i--)
//     {
//         printf("%d ", x[i]);
//     }
//     return 0;
// }

// (5) Program to implement linear search
// #include <stdio.h>

// int main()
// {
//     int n;
//     printf("Enter the size of the array:\n");
//     scanf("%d", &n);
//     int x[n];

//     printf("Enter the elements of the array:\n");
//     for (int i = 0; i < n; i++)
//     {
//         scanf("%d", &x[i]);
//     }

//     int found = 0;
//     int key;
//     printf("Enter the value of the key:\n");
//     scanf("%d", &key);

//     for (int i = 0; i < n; i++)
//     {
//         if (key == x[i])
//         {
//             printf("key matched at index %d.", i);
//             found = 1;
//             break;
//         }
//     }
//     if (found == 0)
//     {
//         printf("key not found.\n");
//     }
//     return 0;
// }

// (6) Program to implement binary search:-
// #include <stdio.h>

// int main()
// {
//     int n;
//     printf("Enter the size of the array:\n");
//     scanf("%d", &n);
//     int x[n];

//     printf("Enter the elements of the array in ascending order:\n");
//     for (int i = 0; i < n; i++)
//     {
//         scanf("%d", &x[i]);
//     }

//     int key;
//     printf("Enter the value of key:\n");
//     scanf("%d", &key);

//     int found = 0, low = 0, high = n - 1;

//     while (low <= high)
//     {
//         int mid = (low + high) / 2;
//         if (key == x[mid])
//         {
//             printf("key found at index %d", mid);
//             found = 1;
//             break;
//         }
//         if (key > x[mid])
//         {
//             low = mid + 1;
//         }
//         if (key < x[mid])
//         {
//             high = mid - 1;
//         }
//     }
//     if (found == 0)
//     {
//         printf("key not found.\n");
//     }
//     return 0;
// }

// (7) Program to implement selection sort:-
// #include <stdio.h>

// int main()
// {
//     int n;
//     printf("Enter the size of the array:\n");
//     scanf("%d", &n);
//     int x[n];

//     printf("Enter the elements of the array:\n");
//     for (int i = 0; i < n; i++)
//     {
//         scanf("%d", &x[i]);
//     }

//     printf("Elements before sorting:\n");
//     for (int i = 0; i < n; i++)
//     {
//         printf("%4d", x[i]);
//     }

//     for (int i = 0; i < n - 1; i++)
//     {
//         for (int j = i+1; j < n; j++)
//         {
//             if (x[j]<x[i])
//             {
//                 int temp;
//                 temp = x[j];
//                 x[j] = x[i];
//                 x[i] = temp;
//             }
//         }
//     }
//     printf("\nElements after sorting:\n");
//     for (int i = 0; i < n; i++)
//     {
//         printf("%4d", x[i]);
//     }
//     return 0;
// }

// (8) Program to implement bubble sort:-
// #include <stdio.h>
// void swap(int *a, int *b)
// {
//     int temp;
//     temp = *a;
//     *a = *b;
//     *b = temp;
// }
// int main()
// {
//     int n;
//     printf("Enter the size of the array:\n");
//     scanf("%d", &n);
//     int x[n];

//     printf("Enter the elements of the array:\n");
//     for (int i = 0; i < n; i++)
//     {
//         scanf("%d", &x[i]);
//     }

//     printf("Elements before sorting:\n");
//     for (int i = 0; i < n; i++)
//     {
//         printf("%4d", x[i]);
//     }

//     for (int i = 0; i < n; i++)
//     {
//         for (int j = 0; j < n - i - 1; j++)
//         {
//             if (x[j] > x[j + 1])
//             {
//                 swap(&x[j], &x[j + 1]);
//             }
//         }
//     }
//     printf("\nElements after sorting:\n");
//     for (int i = 0; i < n; i++)
//     {
//         printf("%4d", x[i]);
//     }
//     return 0;
// }

// (9) Program to add two m x n Matrices:-
// #include <stdio.h>

// int main()
// {
//     int m, n;
//     printf("Enter the number of rows and columns of both matrices:\n");
//     scanf("%d %d", &m, &n);
//     int x[m][n];
//     int y[m][n];

//     printf("Enter the elements of matrix-x:\n");
//     for (int i = 0; i < m; i++)
//     {
//         for (int j = 0; j < n; j++)
//         {
//             scanf("%d", &x[i][j]);
//         }
//     }
//     printf("Enter the elements of matrix-y:\n");
//     for (int i = 0; i < m; i++)
//     {
//         for (int j = 0; j < n; j++)
//         {
//             scanf("%d", &y[i][j]);
//         }
//     }
//     int sum[m][n];
//     for (int i = 0; i < m; i++)
//     {
//         for (int j = 0; j < n; j++)
//         {
//             sum[i][j] = x[i][j] + y[i][j];
//         }
//     }
//     printf("Sum of matrices x and y is:\n");
//     for (int i = 0; i < m; i++)
//     {
//         for (int j = 0; j < n; j++)
//         {
//             printf("%4d", sum[i][j]);
//         }
//         printf("\n");
//     }
//     return 0;
// }

// // (10) Program to multiply two m x n matrices:-
// #include <stdio.h>
// int main()
// {
//     int i, j, k, m, n, p, q;
//     printf("enter the size of matrix a: ");
//     scanf("%d %d", &m, &n);
//     printf("\nenter the size of matrix b: ");
//     scanf("%d %d", &p, &q);
//     if (n != p)
//         printf("\nmatrix multiplication is not possible");
//     if (n == p)
//     {
//         int a[m][n], b[p][q], c[m][q];
//         printf("\nenter the elements of the matrix a: ");
//         for (i = 0; i < m; i++)
//         {
//             for (j = 0; j < n; j++)
//             {
//                 scanf("%d", &a[i][j]);
//             }
//         }
//         printf("\nenter the elements of the matrix b: ");
//         for (i = 0; i < p; i++)
//         {
//             for (j = 0; j < q; j++)
//             {
//                 scanf("%d", &b[i][j]);
//             }
//         }
//         for (i = 0; i < m; i++)
//         {
//             for (j = 0; j < q; j++)
//             {
//                 c[i][j] = 0;
//                 for (k = 0; k < n; k++)
//                 {
//                     c[i][j] = c[i][j] + a[i][k] * b[k][j];
//                 }
//             }
//         }
//         printf("\nthe multiplication of a and b is:-\n");
//         for (i = 0; i < m; i++)
//         {
//             for (j = 0; j < q; j++)
//             {
//                 printf("%d ", c[i][j]);
//             }
//             printf("\n");
//         }
//     }
//     return 0;
// }

// #include <stdio.h>
// #include <string.h>

// int main()
// {
//     char s1[10];
//     gets(s1);
//     //printf();
//     puts(s1);
//     return 0;
// }

// #include <stdio.h>
// #include <string.h>
// int main()
// {
//     char s[50];
//     char s1[50];
//     printf("Enter a line of text: ");
//     gets(s);
//     strcpy(s1, strrev(s));
//     printf("\nThe reverse string is: %s\n", s1);
//     strrev(s);
//     puts(s);
//     if (strcmp(s,s1) == 0)
//         printf("\npalindrome");
//     else
//         printf("\nnot a palindrome");
//     return 0;
// }

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int num;
    int low, high;
    printf("Enter lower and higher value to produce a random number in that range:\n");
    scanf("%d %d", &low, &high);
    srand(time(NULL));
    num = rand()%(high-low+1)+low;
    printf("%d\n", num);
    return 0;
}