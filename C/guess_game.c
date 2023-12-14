#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int number, guess, nguesses=0;
    srand(time(1));
    number = rand()%100+1;
    do {
        printf("Guess the number between 1 to 100 in least possible guesses.\n");
        scanf("%d", &guess);
        nguesses++;
        if (guess>number) {
            printf("Lower number please!\n");
        }
        else if(guess<number) {
            printf("Higher number please!\n");
        }
        else {
            printf("You guessed it in %d attempts\n", nguesses);
        }
    } while(guess!=number);
    return 0;
}