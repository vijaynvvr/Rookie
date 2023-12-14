// Classificaction of functions:-

// 1) Function without parameters and without return type:-

// #include <stdio.h>
// void largest();
// int main()
// {
//     largest();
//     return 0;
// }
// void largest() {
//     int a, b, c, max;
//     printf("Enter three numbers:\n");
//     scanf("%d %d %d", &a, &b, &c);
//     max = a;
//     if (b>max)
//     max = b;
//     if (c>max)
//     max = c;
//     printf("Largest of above numbers is %d", max);
// }

// 2) Function with parameters and without return type:-

// #include <stdio.h>
// void largest(int a, int b, int c);
// int main()
// {
//     int a, b, c;
//     printf("Enter three numbers:\n");
//     scanf("%d %d %d", &a, &b, &c);
//     largest(a, b, c);
//     return 0;
// }
// void largest(int a, int b, int c) {
//     int max;
//     max = a;
//     if (b>max)
//     max = b;
//     if (c>max)
//     max = c;
//     printf("Largest of above numbers is %d", max);
// }

// 3) Function without parameters and with return type:-

// #include <stdio.h>
// int largest();
// int main()
// {
//     int l;
//     l=largest();
//     printf("Largest of above numbers is %d", l);
//     return 0;
// }
// int largest() {
//     int a, b, c, max;
//     printf("Enter three numbers:\n");
//     scanf("%d %d %d", &a, &b, &c);
//     max = a;
//     if (b>max)
//     max = b;
//     if (c>max)
//     max = c;
//     return max;
// }

// 4) Function with parameters and with return type:-

// #include <stdio.h>
// int largest(int a, int b, int c);
// int main()
// {
//     int a, b, c, max;
//     printf("Enter three numbers:\n");
//     scanf("%d %d %d", &a, &b, &c);
//     max = (int)largest(a, b, c);
//     printf("Largest of above numbers is %d", max);
//     return 0;
// }
// int largest(int a, int b, int c) {
//     int max;
//     max = a;
//     if (b>max)
//     max = b;
//     if (c>max)
//     max = c;
//     return max;
// }

// Call by value:-

// #include <stdio.h>
// void change(int num) {
//     printf("Before adding value inside function, num = %d\n", num);
//     num+=100;
//     printf("After adding value inside function, num = %d\n", num);
// }
// int main()
// {
//     int x = 100;
//     printf("Before function call x = %d\n", x);
//     change(x);
//     printf("After function call x = %d\n", x);
//     return 0;
// }

// Call by reference:-

// #include <stdio.h>
// void swap(int *a, int *b) {
//     int temp;
//     temp = *a;
//     *a = *b;
//     *b = temp;
//     printf("After swapping values in function, a = %d b = %d\n", *a, *b);
// }

// int main()
// {
//     int a = 10, b = 20;
//     printf("Before swapping a = %d, b = %d\n", a, b);
//     swap(&a,&b);
//     printf("After swapping a = %d, b = %d\n", a, b);
//     return 0;
// }

// Program to find factorial of a number using recursion:-

// #include <stdio.h>
// int fact(int n);
// int main()
// {
//     int n,f;
//     printf("Enter a number:\n");
//     scanf("%d", &n);
//     f = fact(n);
//     printf("Factorial of the number = %d", f);
//     return 0;
// }
// int fact(int n) {
//     int f;
//     if (n==0) {
//         return 1;
//     }
//     else {
//         f = n*fact(n-1);
//         return f;
//     }
// }

// Program to find sum of digits of a number using recursion:-

// #include <stdio.h>
// int sum(int n);
// int main()
// {
//     int num, s;
//     printf("Enter a number:\n");
//     scanf("%d", &num);
//     s = sum(num);
//     printf("Sum of digits is %d", s);
//     return 0;
// }
// int sum(int n) {
//     int s;
//     if (n==0) {
//         return 0;
//     }
//     else {
//         s = n%10 + sum(n/10);
//         return s;
//     }
// }

// Storage classes:-

// #include <stdio.h>
// extern int i = 10;
// void show()
// {
//     printf("extern i within show() = %d \n", i);
// }
// void display()
// {
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