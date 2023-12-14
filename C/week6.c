// (1) Reverse of number using function with arguments and no return:-
// #include <stdio.h>
// void reverse(int n);
// int main()
// {
//     int a;
//     printf("Enter a number:\n");
//     scanf("%d", &a);
//     reverse(a);
//     return 0;
// }
// void reverse(int n)
// {
//     int num, rem, rev = 0;
//     num = n;
//     while (n != 0)
//     {
//         rem = n % 10;
//         rev = rev * 10 + rem;
//         n = n / 10;
//     }
//     printf("Reverse of %d is %d.", num, rev);
// }

// (2) Program to find whether a given number is a perfect number or not using function with arguments and return type:-
// #include <stdio.h>
// int perfectnum(int n);
// int main()
// {
//     int a, num;
//     printf("Enter a number to check if it is a perfect number:\n");
//     scanf("%d", &a);
//     num = perfectnum(a);
//     if (num)
//     {
//         printf("%d is a perfect number.", a);
//     }
//     else
//     {
//         printf("%d is a not perfect number.", a);
//     }
//     return 0;
// }
// int perfectnum(int n)
// {
//     int divsum = 0;
//     for (int div = 1; div < n; div++)
//     {
//         if (n % div == 0)
//         {
//             divsum = divsum + div;
//         }
//     }
//     if (n == divsum)
//     {
//         return 1;
//     }
//     else
//     {
//         return 0;
//     }
// }

// (3) Program to check if number is armstrong number using a function with no arguments and no return type:-
// #include <stdio.h>
// void armstrong();
// int main()
// {
//     int x;
//     armstrong(x);
//     return 0;
// }
// void armstrong()
// {
//     int n, num, rem, remsum = 0;
//     printf("Enter a number to check if it is an armstrong number:\n");
//     scanf("%d", &n);
//     num = n;
//     while (n != 0)
//     {
//         rem = n % 10;
//         remsum = remsum + rem * rem * rem;
//         n = n / 10;
//     }
//     if (num == remsum)
//     {
//         printf("%d is an armstrong number.", num);
//     }
//     else
//     {
//         printf("%d is not an armstong number.", num);
//     }
// }

// (4) Program to find area of a square using Function with no arguments and with return type:-
// #include <stdio.h>
// int area_sq();
// int main()
// {
//     int a, area;
//     area = area_sq(a);
//     printf("Area of square is %d.", area);
//     return 0;
// }
// int area_sq()
// {
//     int a, area;
//     printf("Enter side length of square:\n");
//     scanf("%d", &a);
//     area = a * a;
//     return area;
// }

// (5) Program to swap the values of two variables using call by value:-
// #include <stdio.h>
// void swap(int a, int b)
// {
//     int temp;
//     temp = a;
//     a = b;
//     b = temp;
//     printf("After swapping values in function, a = %d b = %d\n", a, b);
// }
// int main()
// {
//     int a = 5, b = 10;
//     printf("Before swapping a = %d, b = %d\n", a, b);
//     swap(a, b);
//     printf("After swapping a = %d, b = %d\n", a, b);
//     return 0;
// }

// (6)  Program to swap the values of two variables using call by reference:-
// #include <stdio.h>
// void swap(int *a, int *b)
// {
//     int temp;
//     temp = *a;
//     *a = *b;
//     *b = temp;
//     printf("After swapping values in function, a = %d b = %d\n", *a, *b);
// }
// int main()
// {
//     int a = 5, b = 10;
//     printf("Before swapping a = %d, b = %d\n", a, b);
//     swap(&a, &b);
//     printf("After swapping a = %d, b = %d\n", a, b);
//     return 0;
// }

// (7)  Program to find factorial of a number using recursion.
// #include <stdio.h>
// int fact(int n)
// {
//     int f;
//     if (n == 0)
//     {
//         return 1;
//     }
//     else
//     {
//         f = n * fact(n - 1);
//         return f;
//     }
// }
// int main()
// {
//     int n, f;
//     printf("Enter a number:\n");
//     scanf("%d", &n);
//     f = fact(n);
//     printf("Factorial of the number = %d", f);
//     return 0;
// }

// (8) Write a Program to find the sum of digits of a number using recursion:-
// #include <stdio.h>
// int sum(int n)
// {
//     int s;
//     if (n == 0)
//     {
//         return 0;
//     }
//     else
//     {
//         s = n % 10 + sum(n / 10);
//         return s;
//     }
// }
// int main()
// {
//     int num, s;
//     printf("Enter a number:\n");
//     scanf("%d", &num);
//     s = sum(num);
//     printf("Sum of digits is %d", s);
//     return 0;
// }

// (9) Program to generate Fibonacci series using recursion:-
// #include <stdio.h>
// int fib(int f);
// int main()
// {
//     int i, n, x;
//     printf("Enter the value of n.\n");
//     scanf("%d", &n);
//     printf("The first %d terms of fibonacci series are:\n", n);
//     for (i = 1; i <= n; i++)
//     {
//         x = fib(i);
//         printf("%d ", x);
//     }
//     return 0;
// }
// int fib(int f)
// {
//     int l;
//     if (f == 0)
//         return 0;
//     if (f == 1)
//         return 1;
//     else
//         l = fib(f - 1) + fib(f - 2);
//     return l;
// }

// (10) Program to illustrate auto, static, extern and register storage classes:-
// #include <stdio.h>
// extern int i = 10;
// void show() {
//     printf("extern i within show() = %d \n", i);
// }
// void display() {
//     int j = 5;
//     static int k = 5;
//     j++;
//     printf("auto variable j = %d \n", j);
//     k++;
//     printf("static variable k = %d \n", k);
// }
// int main()
// {
//     register int l = 10;
//     printf("register variable l = %d \n", l);
//     printf("extern i in main() = %d \n", i);
//     show();
//     printf("\n After first call to display() \n");
//     display();
//     printf("\n After second call to display() \n");
//     display();
//     return 0;
// }