//(1) String Initialization:-
// #include <stdio.h>
// int main()
// {
//     char s1[10] = {"welcome"};
//     char s2[10] = {'a', 'd', 'f', 'g', '\0'};
//     char s3[] = {"welcome"};
//     char s4[] = {"programming with strings"};
//     printf("s1=%s\n", s1);
//     printf("s2=%s\n", s2);
//     printf("s3=%s\n", s3);
//     printf("s4=%s\n", s4);
//     printf("size of s1 is %d\n ", sizeof(s1));
//     printf("size of s2 is %d\n ", sizeof(s2));
//     printf("size of s3 is %d\n ", sizeof(s3));
//     printf("size of s4 is %d\n ", sizeof(s4));
//     return 0;
// }

// (2) getchar and putchar:-
// #include <stdio.h>
// int main()
// {
//     char text[80], c;
//     int i;
//     printf("Enter a line of text:\n");
//     i = 0;
//     c = getchar();
//     while (c != '\n')
//     {
//         text[i] = c;
//         c = getchar();
//         i++;
//     }
//     text[i] = '\0';
//     printf("The line of text entered is:\n");
//     for (i = 0; text[i] != '\0'; i++)
//         putchar(text[i]);
//     return 0;
// }

// (3) gets and puts:-
// #include <stdio.h>
// int main()
// {
//     char name[50];
//     printf("Enter your name: ");
//     gets(name);
//     printf("Your name is: ");
//     puts(name);
//     return 0;
// }

// (4) String length without string functions:-
// #include <stdio.h>
// int main()
// {

//     char str[100], length = 0;
//     printf("Enter text: \n");
//     gets(str);
//     while (str[length] != '\0')
//     {
//         length++;
//     }
//     printf("Length of string is %d.", length);
//     return 0;
// }

// (5) Occurance of a character in a string:-
// #include <stdio.h>
// int main()
// {
//     char str[20], ch;
//     int i, count = 0;
//     printf("Enter a string: \n");
//     gets(str);
//     printf("Enter char to find its frequency: ");
//     scanf("%c", &ch);
//     for (int i = 0; str[i] != '\0'; i++)
//     {
//         if (ch == str[i])
//             ++count;
//     }
//     printf("Frequency of %c =%d", ch, count);
//     return 0;
// }

// (6) No. of lowercase,Uppercase,digits,special characters in a line of text:-
// #include <stdio.h>
// int main()
// {
//     char str[40];
//     int i;
//     int upper = 0, lower = 0, digit = 0, special = 0;
//     printf("Please enter the string: \n");
//     gets(str);
//     for (i = 0; str[i] != '\0'; i++)
//     {
//         if (str[i] >= 'A' && str[i] <= 'Z')
//         {
//             upper++;
//         }
//         else if (str[i] >= 'a' && str[i] <= 'z')
//         {
//             lower++;
//         }
//         else if (str[i] >= '0' && str[i] <= '9')
//         {
//             digit++;
//         }
//         else
//             special++;
//         {
//         }
//     }
//     printf("\n upper case letters %d", upper);
//     printf("\n lower case letters %d", lower);
//     printf("\n digits %d", digit);
//     printf("\n special characters %d", special);
//     return 0;
// }

// (7) Sorting character array using bubble sort:-
// #include <stdio.h>
// #include <string.h>
// int main()
// {
//     char s[10][30], t[30];
//     int i, j, n;
//     printf("How many strings:?");
//     scanf("%d", &n);
//     printf("Enter the strings:");
//     for (i = 0; i < n; i++)
//         scanf("%s", s[i]);
//     for (i = 0; i < n - 1; i++)
//         for (j = j + 1; j < n; j++)
//             if (strcmp(s[i], s[j]) > 0)
//             {
//                 strcpy(t, s[i]);
//                 strcpy(s[i], s[j]);
//                 strcpy(s[j], t);
//             }
//     for (i = 0; i < n; i++)
//         printf("\n%s", s[i]);
//     return 0;
// }

// (8) Illustrate Strcmp() and Strcpy() in built functions:-
// #include <stdio.h>
// #include <string.h>
// int main()
// {
//     char x[50];
//     char y[] = "a programming example";
//     strcpy(x, "A programming example");
//     if (strcmp(x, "A programming example") == 0)
//         printf("Equal\n");
//     else
//         printf("Unequal\n");
//     if (strcmp(y, x) == 0)
//         printf("Equal\n");
//     else
//         printf("Unequal\n");
//     return 0;
// }

// (9) String is palindrome or not with strrev():-
// #include <stdio.h>
// #include <string.h>
// int main()
// {
//     char a[100], b[100];
//     printf("Enter a string to check if its a palindrome: ");
//     gets(a);
//     strcpy(b, a);
//     strrev(b);
//     if (strcmp(a, b) == 0)
//         printf("The string is a palindrome\n");
//     else
//         printf("The string isnt a palindrome\n");
//     return 0;
// }

// (10) String is palindrome or not without using strrev().
#include <stdio.h>
int main()
{
    char text[100];
    int begin, middle, end, length = 0;
    printf("Enter text: \n");
    gets(text);
    while (text[length] != '\0')
        length++;
    end = length - 1;
    middle = length / 2;
    for (begin = 0; begin < middle; begin++)
    {
        if (text[begin] != text[end])
        {
            printf("Not a palindrome");
            break;
        }
        end--;
    }
    if (begin == middle)
        printf("Palindrome");
    return 0;
}