#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));
    int you, comp;
    printf("\n~~~~~~~~~~~~~~~~~~~~~~~~HAND CRICKET~~~~~~~~~~~~~~~~~~~~~~~~\n");
    printf("RULES:\n");
    printf("1)You can select numbers from 1 to 6, same applies for computer.\n");
    printf("2)You can choose to either bat or to bowl if you win the toss.\n");
    printf("3)The batsman gets out if the number chosen by both batsman and bowler are same.\n");
    printf("4)Batsman goes on scoring runs until he gets out.\n");
    printf("5)The numbers that he opts while batting goes on adding until he gets out.\n");
    printf("6)Batting first? Post a huge target. Bowling first? Chase down the target.\n");
    printf("\nLet's get started!\n");

    int toss, youToss, compToss, choose, compBatOrBowl, youBatOrBowl, flag;
    toss = rand() % 2;
    compToss = rand() % 2;
    compBatOrBowl = rand() % 2;
    printf("You wanna choose the toss? or let the computer choose?\n");
    printf("Enter \"1\" if you wanna choose and \"0\" if you want computer to choose:\n");
    scanf("%d", &choose);
    if (choose == 1)
    {
        printf("So you wanna choose the toss? Cool!\n");
    }
    else
    {
        printf("Damn! You are letting our poor computer to choose the toss!\n");
    }
    switch (choose)
    {
    case 0:
        if (compToss == toss)
        {
            flag = 0;
            switch (compToss)
            {
            case 0:
                printf("Computer choose tails, and tails it is!\n");
                printf("Computer won the toss!\n");
                break;
            case 1:
                printf("Computer choose heads, and heads it is!\n");
                printf("Computer won the toss!\n");
                break;
            }
        }
        else
        {
            flag = 1;
            switch (compToss)
            {
            case 0:
                printf("Computer choose tails, and heads it is!\n");
                printf("Computer lost the toss!\n");
                break;
            case 1:
                printf("Computer choose heads, and tails it is!\n");
                printf("Computer lost the toss!\n");
                break;
            }
        }
        break;
    case 1:
        printf("Choose \"1\" for heads and \"0\" for tails:\n");
        scanf("%d", &youToss);
        if (youToss == toss)
        {
            flag = 1;
            switch (youToss)
            {
            case 0:
                printf("You choose tails, and tails it is!\n");
                printf("You won the toss!\n");
                break;
            case 1:
                printf("You choose heads, and heads it is!\n");
                printf("You won the toss!\n");
                break;
            }
        }
        else
        {
            flag = 0;
            switch (youToss)
            {
            case 0:
                printf("You choose tails, and heads it is!\n");
                printf("You lost the toss!\n");
                break;
            case 1:
                printf("You choose heads, and tails it is!\n");
                printf("You lost the toss!\n");
                break;
            default:
                printf("Invalid option :/");
                exit(0);
            }
        }
        break;
    default:
        printf("Invalid option :/");
        exit(0);
    }
    switch (flag)
    {
    case 0:
        if (compBatOrBowl == 1)
        {
            flag = 2;
            printf("And as computer won the toss, he chose to BAT, and you gonna BOWL!\n");
        }
        else
        {
            flag = 3;
            printf("And as computer won the toss, he chose to BOWL, and you gonna BAT!\n");
        }
        break;
    case 1:
        printf("Choose \"1\" to BAT and \"0\" to BOWL:\n");
        scanf("%d", &youBatOrBowl);
        if (youBatOrBowl == 1)
        {
            flag = 3;
            printf("Pad up buddy! As you won the toss, you chose to BAT!\n");
        }
        else
        {
            flag = 2;
            printf("Ready to bowl them out? As you won the toss, you chose to BOWL!\n");
        }
        break;
    }

    int compscore = 0;
    int youscore = 0;

    switch (flag)
    {
    case 2: // Computer bats first, you bowl first.
        while (flag == 2)
        {
            comp = rand() % 6 + 1;
            printf("\nChoose any number from 1 to 6: \n");
        a:
            scanf("%d", &you);
            if (you < 1 || you > 6)
            {
                printf("Please follow the rules!, choose again.\n");
                goto a;
            }
            printf("Computer chose %d.\n", comp);
            printf("You chose %d.\n", you);
            if (you != comp)
            {
                printf("Computer scored %d runs!\n", comp);
                compscore += comp;
            }
            else
            {
                printf("Computer is OUT!\n");
                printf("Computer posted a total of %d runs!\n", compscore);
                break;
            }
            printf("Computer score: %d runs.\n", compscore);
            if (compscore >= 50 && compscore < 100)
            {
                printf("\nIt's a HALF CENTURY for computer!!\n");
            }
            if (compscore >= 100)
            {
                printf("\nIt's a CENTURY for our computer!!!\n");
            }
        }
        printf("\nYour target is %d runs.\n", compscore + 1);
        while (youscore <= compscore)
        {
            comp = rand() % 6 + 1;
            printf("\nChoose any number from 1 to 6: \n");
        b:
            scanf("%d", &you);
            if (you < 1 || you > 6)
            {
                printf("Please follow the rules!, choose again.\n");
                goto b;
            }
            printf("You chose %d.\n", you);
            printf("Computer chose %d.\n", comp);
            if (you != comp)
            {
                printf("You scored %d runs!\n", you);
                youscore += you;
            }
            else if (youscore == compscore)
            {
                printf("You are OUT!\n");
                printf("\nDamn! It's a tie.\n");
                break;
            }
            else if (youscore < compscore)
            {
                printf("You are OUT!\n");
                printf("\nComputer won by %d runs!\n", compscore - youscore);
                break;
            }
            printf("Your score: %d runs.\n", youscore);
            if (youscore <= compscore)
                printf("You need more %d runs required to WIN.\n", compscore - youscore + 1);
            if (youscore >= 50 && youscore < 100)
            {
                printf("\nLift your bat buddy! It's a HALF CENTURY!!\n");
            }
            if (youscore >= 100)
            {
                printf("\nTime to take your helmet off! It's a CENTURY!!!\n");
            }
        }
        if (youscore > compscore)
        {
            printf("\nYou WON against our computer!\n");
        }
        break;
    case 3: // Computer bowls first, you bat first.
        while (flag == 3)
        {
            comp = rand() % 6 + 1;
            printf("\nChoose any number from 1 to 6: \n");
        c:
            scanf("%d", &you);
            if (you < 1 || you > 6)
            {
                printf("Please follow the rules!, choose again.\n");
                goto c;
            }
            printf("You chose %d.\n", you);
            printf("Computer chose %d.\n", comp);
            if (you != comp)
            {
                printf("You scored %d runs!\n", you);
                youscore += you;
            }
            else
            {
                printf("You are OUT!\n");
                printf("You have posted a total of %d runs!\n", youscore);
                break;
            }
            printf("Your score: %d runs.\n", youscore);
            if (youscore >= 50 && youscore < 100)
            {
                printf("\nLift your bat buddy! It's a HALF CENTURY!!\n");
            }
            if (youscore >= 100)
            {
                printf("\nTime to take your helmet off! It's a CENTURY!!!\n");
            }
        }
        printf("\nComputer's target is %d runs.\n", youscore + 1);
        while (compscore <= youscore)
        {
            comp = rand() % 6 + 1;
            printf("\nChoose any number from 1 to 6: \n");
        d:
            scanf("%d", &you);
            if (you < 1 || you > 6)
            {
                printf("Please follow the rules!, choose again.\n");
                goto d;
            }
            printf("Computer chose %d.\n", comp);
            printf("You chose %d.\n", you);
            if (comp != you)
            {
                printf("Computer scored %d runs!\n", comp);
                compscore += comp;
            }
            else if (youscore == compscore)
            {
                printf("Computer is OUT!\n");
                printf("\nDamn! It's a tie.\n");
                break;
            }
            else if (compscore < youscore)
            {
                printf("Computer is OUT!\n");
                printf("\nYou WON by %d runs!\n", youscore - compscore);
                break;
            }
            printf("Computer score: %d runs.\n", compscore);
            if (compscore <= youscore)
                printf("Computer needs more %d runs required to WIN.\n", youscore - compscore + 1);
            if (compscore >= 50 && compscore < 100)
            {
                printf("\nIt's a HALF CENTURY for computer!!\n");
            }
            if (compscore >= 100)
            {
                printf("\nIt's a CENTURY for our computer!!!\n");
            }
        }
        if (compscore > youscore)
        {
            printf("\nComputer WON against you!\n");
        }
    }
    return 0;
}