#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>
#define NO_OF_WORKING_DAYS 100
#define MAX_SIZE 100

struct StudentResult
{
    int marks1;
    int marks2;
    int marks3;
    int marks4;
    int marks5;
    char result[10];
};

struct StudentMaster
{
    char stud_hallticket[10];
    char stud_name[50];
    char stud_address[50];
    char stud_class[25];
    char stud_fees_status[1];
    int number_of_days_present;
    struct StudentResult sm;
};
struct StudentMaster stud[MAX_SIZE];

void getStudentResult(struct StudentResult *s)
{
    printf("\t ------------------------------------\n");
    printf("\t Enter the Subject 1 Marks\n");
    scanf("%d", &s->marks1);
    printf("\t Enter the Subject 2 Marks\n");
    scanf("%d", &s->marks2);
    printf("\t Enter the Subject 3 Marks\n");
    scanf("%d", &s->marks3);
    printf("\t Enter the Subject 4 Marks\n");
    scanf("%d", &s->marks4);
    printf("\t Enter the Subject 5 Marks\n");
    scanf("%d", &s->marks5);
}

void calculateStudentResult(struct StudentResult *s)
{
    if (s->marks1 >= 50 && s->marks2 >= 50 && s->marks3 >= 50 && s->marks4 >= 50 && s->marks5 >= 50)
    {
        strcpy(s->result, "PASS");
    }
    else
    {
        strcpy(s->result, "FAIL");
    }
}
void displayStudentResult(struct StudentMaster obj)
{

    printf("%s\t", obj.stud_hallticket);
    printf("%s\t", obj.stud_name);
    printf("%s\n", obj.sm.result);
}
void getStudentData(struct StudentMaster *obj)
{
    printf("\t ------------------------------------\n");
    printf("\t Enter the Student Hall Ticket Number\n");
    scanf("%s", obj->stud_hallticket);
    printf("\t Enter the Student Name\n");
    scanf("%s", obj->stud_name);
    printf("\t Enter the Student Address\n");
    scanf("%s", obj->stud_address);
    printf("\t Enter the Student Class\n");
    scanf("%s", obj->stud_class);
    printf("\t Enter the Student Fees Status P for Paid and N for Not Paid\n");
    scanf("%s", obj->stud_fees_status);
    printf("\t Enter the Student Number of days Present\n");
    scanf("%d", &obj->number_of_days_present);
}
void displayData(struct StudentMaster obj1)
{
    printf("\t ------------------------------------\n");
    printf("The Student Hall Ticket Number:\t");
    printf("%s\n", obj1.stud_hallticket);
    printf(" The Student Name:\t");
    printf("%s \n", obj1.stud_name);
    printf(" The Student Address:\t");
    printf("%s \n", obj1.stud_address);
    printf("The Student Class:\t");
    printf("%s \n", obj1.stud_class);
    printf("The Student Fees Status P for Paid and N for Not Paid:\t");
    printf("%c \n", obj1.stud_fees_status[0]);
    printf(" The Student Number of days Present:\t");
    printf("%d \n", obj1.number_of_days_present);
}
void checkElgibility(int n1)
{
    int i;
    float percentage;
    printf("Into the Check Elegibility Function");
    printf("Hall Ticket Number\tStudent Name\tClass\tAttendence Percentage\tFeesStatus\tEligibility\n");
    printf("---------------------------------------------------------------------------------------\n");
    for (i = 0; i <= (n1 - 1); i++)
    {
        percentage = (stud[i].number_of_days_present / (float)NO_OF_WORKING_DAYS) * 100;
        //	printf("%f",percentage);
        if (percentage >= 65 && stud[i].stud_fees_status[0] == 'P')
        {
            printf("%s \t \t \t%s \t %s \t %2f \t PAID \t Eligible\n", stud[i].stud_hallticket, stud[i].stud_name, stud[i].stud_class, percentage);
        }

        else if (percentage <= 65 && stud[i].stud_fees_status[0] == 'P')
        {
            printf("%s \t \t \t%s\t %s \t %2f \t PAID \t Not Eligible\n", stud[i].stud_hallticket, stud[i].stud_name, stud[i].stud_class, percentage);
        }
        else
        {
            printf("%s \t \t\t %s\t %s \t %2f \t NOT PAID \t Not Eligible\n", stud[i].stud_hallticket, stud[i].stud_name, stud[i].stud_class, percentage);
        }

        printf("------------------------------------------------------------------------------------------\n");
    }
}

int main()
{
    int n, i, option;
    float percentage;

    do
    {
        printf("STUDENT EXAMINATION SYSTEM\n");
        printf("---------------------------\n");
        printf("Enter 1 to Get Student Data\n");
        printf("Enter 2 to Display Student Data\n");
        printf("Enter 3 to Check Eligibility of Student\n");
        printf("Enter 4 to Accept the Marks\n");
        printf("Enter 5 to Display the Result\n");
        printf("Enter 6 to Exit\n");
        printf("Enter your choice\n");
        scanf("%d", &option);
        switch (option)
        {
        case 1:
            printf("Enter the strength of the class less than or equal to 100\n");
            scanf("%d", &n);
            for (i = 0; i <= (n - 1); i++)
            {
                getStudentData(&stud[i]);
            }

            break;
        case 2:
            for (i = 0; i <= (n - 1); i++)
            {
                displayData(stud[i]);
            }
            break;
        case 3:
            checkElgibility(n);
            break;
        case 4:
            for (i = 0; i <= (n - 1); i++)
            {
                percentage = (stud[i].number_of_days_present / (float)NO_OF_WORKING_DAYS) * 100;
                if (percentage >= 65 && stud[i].stud_fees_status[0] == 'P')
                {
                    printf("Enter the marks of Student %s\n", stud[i].stud_hallticket);
                    getStudentResult(&stud[i].sm);
                }
            }
            break;
        case 5:
            for (i = 0; i <= (n - 1); i++)
            {
                percentage = (stud[i].number_of_days_present / (float)NO_OF_WORKING_DAYS) * 100;
                if (percentage >= 65 && stud[i].stud_fees_status[0] == 'P')
                {
                    calculateStudentResult(&stud[i].sm);
                }
            }
            printf("\t Student Hall Ticket Number \t Student Name \t Student Result\n");
            printf("\t ------------------------------------------------------------\n");
            for (i = 0; i <= (n - 1); i++)
            {

                percentage = (stud[i].number_of_days_present / (float)NO_OF_WORKING_DAYS) * 100;
                if (percentage >= 65 && stud[i].stud_fees_status[0] == 'P')
                {
                    displayStudentResult(stud[i]);
                }
            }
            break;
        case 6:
            exit(0);
            break;
        }

    } while (option <= 6);
    return 0;
}