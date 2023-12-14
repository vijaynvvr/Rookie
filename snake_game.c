// #include <stdio.h>
// #include <conio.h>
// #include <stdlib.h>
// #include <time.h>

// int height = 25, width = 40;
// int x, y, foodx, foody, score, gamestatus, flag;
// int tailX[100], tailY[100], countTail = 0;

// void setup()
// {
//     gamestatus = 1;
//     x = width / 2;
//     y = height / 2;
//     foodx = rand() % (width - 2) + 1;
//     foody = rand() % (height - 2) + 1;
//     score = 0;
// }

// void draw()
// {
//     int i, j, k;
//     system("cls");
//     printf("\n  C L A S S I C   S N A K E   G A M E\n");
//     printf("\n\t   S C O R E  =  %d\n", score);
//     for (j = 0; j < height; j++)
//     {
//         for (i = 0; i < width; i++)
//         {
//             if (j == 0 || j == (height - 1))
//             {
//                 printf("-");
//             }
//             else if (i == 0 || i == (width - 1))
//             {
//                 printf("|");
//             }
//             else
//             {
//                 if (i == x && j == y)
//                     printf("O");
//                 else if (i == foodx && j == foody)
//                     printf("$");
//                 else
//                 {
//                     int flag = 0;
//                     for (k = 0; k < countTail; k++)
//                     {
//                         if (i == tailX[k] && j == tailY[k])
//                         {
//                             printf("o");
//                             flag = 1;
//                         }
//                     }
//                     if (!flag)
//                         printf(" ");
//                 }
//             }
//         }
//         printf("\n");
//     }
// }

// void input()
// {
//     if (kbhit())
//     {
//         switch (getch())
//         {
//         case 75: //left
//         case 'a':
//             flag = 1;
//             break;
//         case 77: //right
//         case 's':
//             flag = 2;
//             break; 
//         case 72: //up
//         case 'w':
//             flag = 3;
//             break;
//         case 80: //down
//         case 'z':
//             flag = 4;
//             break;
//         case 'e': //exit
//             gamestatus = 0;
//             flag = 5;
//             break;
//         }
//     }
// }

// void logic()
// {
//     int i, tempX, tempY;
//     tailX[0] = x;
//     tailY[0] = y;
//     for(i = 1; i < countTail; i++)
//     {
//         tempX = tailX[i];
//         tempY = tailY[i];
//         tailX[i] = tailX[i-1]; 
//         tailY[i] = tailY[i-1]; 
//         tailX[i-1] = tempX;
//         tailY[i-1] = tempY;
//     }
//     switch (flag)
//     {
//     case 1:
//         x--;
//         break;
//     case 2:
//         x++;
//         break;
//     case 3:
//         y--;
//         break;
//     case 4:
//         y++;
//         break;
//     case 5:
//         gamestatus = 0;
//         break;
//     }
//     if (x <= 0 || x >= width - 1 || y <= 0 || y >= height - 1)
//         gamestatus = 0; //game ends if snake strikes the boundary
//     for (i = 0; i < countTail; i++)
//     {
//         if (x == tailX[i] && y == tailY[i])
//             gamestatus = 0; // game ends if snake bites itself
//     }
//     if (x == foodx && y == foody)
//     {
//         foodx = rand() % (width - 2) + 1;
//         foody = rand() % (height - 2) + 1;
//         score += 10; // score increases bt 10 if snake eats the food
//         countTail++; // length of snake also increases if snake eats food
//     }
// }

// int main()
// {
//     srand(time(0));
//     setup();
//     while (gamestatus)
//     {
//         draw();
//         input();
//         logic();
//     }
//     if (!gamestatus)
//         printf("\n\t  G A M E   O V E R\n");
//     return 0;
// }