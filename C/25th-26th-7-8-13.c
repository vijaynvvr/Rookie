// #include <stdio.h>
// int main() {
//     int n,i;
//     printf("Enter a number:\n");
//     scanf("%d", &n);
    
//     for(i=2; i<n; i++) {
//         if (n%i==0) {
//             printf("Non Prime");
//             break;
//         }
//     }

//     if (n==i) {
//         printf("Prime");
//     }
//     return 0; 
// } 

// #include <stdio.h>
// int main()
// {

//     int n;
//     printf("Enter a number: ");
//     scanf("%d", &n);

//     for (int num = 1; num <= n; num++)
//     {
//         int i;
//         for (i = 2; i < num; i++)
//         {
//             if (num % i == 0)
//             { 
//                 break;
//             }
//         }
//         if (i == num)
//         { 
//             printf("%d\n", num);
//         }
//     }
//     return 0;
// }

// #include <stdio.h>
// int main()
// {

//     int num1, num2;
//     printf("Enter two numbers: ");
//     scanf("%d %d", &num1, &num2);

//     for (int num = num1; num <= num2; num++)
//     {
//         int i;
//         for (i = 2; i < num; i++)
//         {
//             if (num % i == 0)
//             { 
//                 break;
//             }
//         }
//         if (i == num)
//         { 
//             printf("%d\n", num);
//         }
//     }
//     return 0;
// }