#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

int height = 25, width = 40;
int x, y, foodx, foody, score, gamestatus, flag;
int tailX[100], tailY[100], countTail = 0;

void setup()
{
    gamestatus = 1;
    x = width / 2;
    y = height / 2;
    foodx = rand() % (width - 2) + 1;
    foody = rand() % (height - 2) + 1;
    score = 0;
}

void draw()
{
    int i, j, k;
    system("cls");
    for (j = 0; j < height; j++)
    {
        for (i = 0; i < width; i++)
        {
            if (j == 0 || j == (height - 1) || i == 0 || i == (width - 1))
            {
                printf("*");
            }
            else
            {
                if (i == x && j == y)
                    printf("O");
                else if (i == foodx && j == foody)
                    printf("$");
                else
                {
                    int flag = 0;
                    for (k = 0; k < countTail; k++)
                    {
                        if (i == tailX[k] && j == tailY[k])
                        {
                            printf("o");
                            flag = 1;
                        }
                    }
                    if (!flag)
                        printf(" ");
                }
            }
        }
        printf("\n");
    }
    printf("\n\tS C O R E = %d\n", score);
}

void input()
{
    if (kbhit())
    {
        switch (getch())
        {
        case 'a':
            flag = 1;
            break;
        case 's':
            flag = 2;
            break;
        case 'w':
            flag = 3;
            break;
        case 'z':
            flag = 4;
            break;
        case 'e':
            gamestatus = 0;
            break;
        }
    }
}

void logic()
{
    int i;
    int prevX = tailX[0];
    int prevY = tailY[0];
    int prev2X,prev2Y;
    tailX[0] = x;
    tailY[0] = y;
    for(i = 1; i < countTail; i++)
    {
        prev2X = tailX[i];
        prev2Y = tailY[i];
        tailX[i] = prevX;
        tailY[i] = prevY;
        prevX = prev2X;
        prevY = prev2Y;
    }

    switch (flag)
    {
    case 1:
        x--;
        break;
    case 2:
        x++;
        break;
    case 3:
        y--;
        break;
    case 4:
        y++;
        break;
    default:
        break;
    }
    if (x <= 0 || x >= width - 1 || y <= 0 || y >= height - 1)
        gamestatus = 0;
    for (i = 0; i < countTail; i++)
    {
        if (x == tailX[i] && y == tailY[i])
            gamestatus = 0;
    }
    if (x == foodx && y == foody)
    {
        foodx = rand() % (width - 2) + 1;
        foody = rand() % (height - 2) + 1;
        score += 10;
        countTail++;
    }
}

int main()
{
    setup();
    while (gamestatus)
    {
        draw();
        input();
        logic();
    }
    if (!gamestatus)
        printf("\n\tG A M E   O V E R\n");
    return 0;
}