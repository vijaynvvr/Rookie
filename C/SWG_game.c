#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));
    int you;
    int pu = 0, pc = 0;
    printf("\n---SNAKE WATER GUN!!!---\n\n");
    printf("Rules: Snake wins over Water       Water wins over Gun       Gun wins over Snake\n");
    do
    {
        printf("\nChoose following:\n");
        printf("1 for Snake, 2 for Water, 3 for Gun, 4 To Exit.\n\n");
        scanf("%d", &you);
        int comp;
        comp = rand() % 3 + 1;
        switch (you)
        {
        case 1:
            if (comp == 1)
            {
                printf("You chose Snake, Same did the Computer.");
            }
            else if (comp == 2)
            {
                pu++;
                printf("You chose Snake, Computer chose water.");
            }
            else if (comp == 3)
            {
                pc++;
                printf("You chose Snake, Computer chose Gun.");
            }
            break;
        case 2:
            if (comp == 1)
            {
                pc++;
                printf("You chose Water, Computer chose Snake.");
            }
            else if (comp == 2)
            {
                printf("You chose Water, Same did the Computer.");
            }
            else if (comp == 3)
            {
                pu++;
                printf("You chose Water, Computer chose Gun.");
            }
            break;
        case 3:
            if (comp == 1)
            {
                pu++;
                printf("You chose Gun, Computer chose Snake.");
            }
            else if (comp == 2)
            {
                pc++;
                printf("You chose Gun, Computer chose Water.");
            }
            else if (comp == 3)
            {
                printf("You choose Gun, Same did the Computer.");
            }
            break;
        case 4:
            printf("You have exited.");
            break;
        default:
            printf("Please chose valid option!");
        }
        printf("\nYour points: %d, Computer points: %d", pu, pc);
    } while (you != 4);

    if (pu > pc)
    {
        printf("\nYour points: %d, Computer points: %d, And you won with this computer!", pu, pc);
    }
    else if (pu == pc)
    {
        printf("\nYour points: %d, Computer points: %d, It's a draw!", pu, pc);
    }
    else
    {
        printf("\nYour points: %d, Computer points: %d, And you lost with this computer!", pu, pc);
    }
    return 0;
}