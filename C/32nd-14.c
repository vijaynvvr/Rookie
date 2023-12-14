// #include <stdio.h>

// int main()
// {
//     int i,j;
//     for (i=1; i<=4; i++) {
//         for (j=1; j<=i; j++) {
//             printf("%3d", j);
//         }
//         printf("\n");
//     }
//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     int line, n, j;
//     for (line=1; line<=3; line++) {
//         for (n=1; n<=line; n++) {
//             printf("%3d", n);
//         }
//         printf("\n");
//     }
//     for (n=2; n>=1; --n) {
//         for (j=1; j<=n; j++) {
//             printf("%3d", j);
//         }
//         printf("\n");
//     }
//     return 0;
// }

// #include <stdio.h>

// int main()
// {
//     int line, n, gap;
//     for (line=1; line<=3; line++) {
//         for (gap=1; gap<=(3-line); gap++) {
//             printf(" ");
//         }
//         for (n=1; n<=line; n++) {
//             printf("%2d", n);
//         }
//         printf("\n");
//     }
//     return 0;
// }

// #include <stdio.h>

// int main()
// {
//     int line, gap;
//     for (line =1; line<=5; line++) {
//         for (gap=1; gap<=(5-line); gap++) {
//             printf(" ");
//         }
//         printf("*****");
//         printf("\n");
//     }
//     return 0;
// }