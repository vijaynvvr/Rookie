#include <stdio.h>
#include <stdlib.h>
#include <time.h>
void main()
{
    srand(time(0));
    printf("\nGAME RULES: THERE IS AN INITIAL PILE OF MARBLES.\n");
    printf("\n            TOSS WILL DECIDE WHO WILL CHOOSE THE MARBLES FIRST.\n");
    printf("\n            ONE CAN CHOOSE ATLEAST ONE MARBLE AND ATMOST HALF OF THE MARBLES PRESENT AT THE SITUATION.\n");
    int marbles;
    marbles = rand() % (91) + 10;
    printf("\nThe initial size of the pile of marbles is: %d \n", marbles);
    int you, comp;
    int marbles_left = marbles;
    int toss = rand() % 2;
    if (toss)
        printf("\nYou won the toss, first chance to choose the marbles is yours!\n");
    else
        printf("\nYou lost the toss, computer is going to choose the marbles first!\n");
    int compIntelligence = rand() % 2;
    int flag;
    if (compIntelligence)
    {
        printf("\nThe computer is going to play smartly!\n");
        do
        {
            switch (toss)
            {
            case 0:
                if (marbles_left > 63 && marbles_left <= 100)
                    comp = marbles_left - 63;
                if (marbles_left > 31 && marbles_left < 63)
                    comp = marbles_left - 31;
                if (marbles_left > 15 && marbles_left < 31)
                    comp = marbles_left - 15;
                if (marbles_left > 7 && marbles_left < 15)
                    comp = marbles_left - 7;
                if (marbles_left > 3 && marbles_left < 7)
                    comp = marbles_left - 3;
                if (marbles_left > 1 && marbles_left < 3)
                    comp = marbles_left - 1;
                if (marbles_left == 3 || marbles_left == 7 || marbles_left == 15 || marbles_left == 31 || marbles_left == 63)
                    comp = rand() % (marbles_left / 2) + 1;
                marbles_left -= comp;
                printf("\nComputer chose %d marbles\n", comp);
                printf("\n%d marbles left, now your turn.\n", marbles_left);
                flag = 0;
                if (marbles_left == 1)
                    break;
                scanf("%d", &you);
                while (you < 1 || you > marbles_left / 2)
                {
                    printf("\nYou can choose atleast one marble and atmost half of the remaining marbles.\n");
                    printf("\n%d marbles remaining. Please follow above rule, choose your marbles again:\n", marbles_left);
                    scanf("%d", &you);
                }
                printf("\nYou chose %d marbles\n", you);
                marbles_left -= you;
                printf("\n%d marbles left.\n", marbles_left);
                flag = 1;
                break;
            case 1:
                printf("\n%d marbles left, your turn.\n", marbles_left);
                scanf("%d", &you);
                while (you < 1 || you > marbles_left / 2)
                {
                    printf("\nYou can choose atleast one marble and atmost half of the remaining marbles.\n");
                    printf("\n%d marbles remaining. Please follow above rule, choose your marbles again:\n", marbles_left);
                    scanf("%d", &you);
                }
                printf("\nYou chose %d marbles\n", you);
                marbles_left -= you;
                printf("\n%d marbles left.\n", marbles_left);
                flag = 1;
                if (marbles_left == 1)
                    break;
                if (marbles_left > 63 && marbles_left <= 100)
                    comp = marbles_left - 63;
                if (marbles_left > 31 && marbles_left < 63)
                    comp = marbles_left - 31;
                if (marbles_left > 15 && marbles_left < 31)
                    comp = marbles_left - 15;
                if (marbles_left > 7 && marbles_left < 15)
                    comp = marbles_left - 7;
                if (marbles_left > 3 && marbles_left < 7)
                    comp = marbles_left - 3;
                if (marbles_left > 1 && marbles_left < 3)
                    comp = marbles_left - 1;
                if (marbles_left == 3 || marbles_left == 7 || marbles_left == 15 || marbles_left == 31 || marbles_left == 63)
                    comp = rand() % (marbles_left / 2) + 1;
                if (marbles_left == 1)
                    break;
                printf("\nComputer chose %d marbles\n", comp);
                marbles_left -= comp;
                flag = 0;
                break;
            }
        } while (marbles_left != 1);
    }
// ~by vj
    else
    {
        printf("\nThe computer is going to play stupidly.\n");
        do
        {
            switch (toss)
            {
            case 0:
                comp = rand() % (marbles_left / 2) + 1;
                marbles_left -= comp;
                printf("\nComputer chose %d marbles\n", comp);
                printf("\n%d marbles left, now your turn.\n", marbles_left);
                flag = 0;
                if (marbles_left == 1)
                    break;
                scanf("%d", &you);
                while (you < 1 || you > marbles_left / 2)
                {
                    printf("\nYou can choose atleast one marble and atmost half of the remaining marbles.\n");
                    printf("\n%d marbles remaining. Please follow above rule, choose your marbles again:\n", marbles_left);
                    scanf("%d", &you);
                }
                printf("\nYou chose %d marbles\n", you);
                marbles_left -= you;
                printf("\n%d marbles left.\n", marbles_left);
                flag = 1;
                break;
            case 1:
                printf("\n%d marbles left, your turn.\n", marbles_left);
                scanf("%d", &you);
                while (you < 1 || you > marbles_left / 2)
                {
                    printf("\nYou can choose atleast one marble and atmost half of the remaining marbles.\n");
                    printf("\n%d marbles remaining. Please follow above rule, choose your marbles again:\n", marbles_left);
                    scanf("%d", &you);
                }
                printf("\nYou chose %d marbles\n", you);
                marbles_left -= you;
                printf("\n%d marbles left.\n", marbles_left);
                flag = 1;
                if (marbles_left == 1)
                    break;
                comp = rand() % (marbles_left / 2) + 1;
                printf("\nComputer chose %d marbles\n", comp);
                marbles_left -= comp;
                flag = 0;
                break;
            }
        } while (marbles_left != 1);
    }
    if (flag)
        printf("\nYou won the game!");
    else
        printf("\nYou lost the game.\n");
}